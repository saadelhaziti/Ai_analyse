import io
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_huggingface import HuggingFaceEmbeddings
from DB_Save.controller.Minio_controller import Get_file_from_minio, POST_file_in_Minio
from users.services.Project_Services import get_project
from sqlalchemy.orm import Session
from DB_Save.routes import get_db
from fastapi import Depends
from DB_Save.Models_save.Minio import MinIOStorage



class RetailRAG:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2"
        )
        self.llm = OllamaLLM(model="mistral:7b")
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer",
        )
        self.conversation_store = "conversations.json"
        self.guid_project = None
        self.db = get_db()
        self.clear_memory()


    def set_conversation_id(self, guid_project: str, db: Session = Depends(get_db)):
        self.guid_project = guid_project
        self.db = db

    def load_conversation_history(self) -> List[Dict]:
        proj = get_project(self.db, self.guid_project)
        user_id = str(proj.guid_user)
        key_path = f"{user_id}/{self.guid_project}/conversations.json"
        minio_storage = MinIOStorage()

        if not minio_storage.exists(key_path):
            return []

        try:
            file_stream, _ = Get_file_from_minio(key_path)

            if file_stream:
                conversations = file_stream.read().decode('utf-8')
                return json.loads(conversations)
        except FileNotFoundError:
            return []

        return []
        

    def load_existing_conversation(self) -> bool:
        conversations = self.load_conversation_history()
        if not conversations:
            return False

        for exchange in conversations:
            if "question" in exchange and "answer" in exchange:
                self.memory.chat_memory.add_user_message(exchange["question"])
                self.memory.chat_memory.add_ai_message(exchange["answer"])
        return True

    def save_conversation(self, question: str, answer: str):
        conversations = self.load_conversation_history()

        if not isinstance(conversations, list):
            conversations = []

        conversations.append({
            "timestamp": datetime.now().isoformat(),
            "question": question,
            "answer": answer
        })

        proj = get_project(self.db, self.guid_project)
        user_id = str(proj.guid_user)
        key_path = f"{user_id}/{self.guid_project}/conversations.json"

        json_data = json.dumps(conversations, indent=2)
        POST_file_in_Minio(io.BytesIO(json_data.encode("utf-8")), key_path, "application/json")



    def setup_vectorstore(self):
        base_dir = Path(__file__).resolve().parent
        persist_dir = base_dir / "retail_data_store"
        index_name = "retail_faiss_index"
        faiss_file = persist_dir / f"{index_name}.faiss"
        pkl_file = persist_dir / f"{index_name}.pkl"

        if not faiss_file.exists() or not pkl_file.exists():
            raise FileNotFoundError("FAISS index files are missing. Cannot proceed.")

        vectorstore = FAISS.load_local(
            folder_path=str(persist_dir),
            index_name=index_name,
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True,
        )
        return vectorstore

    def check_question_relevance(self, question, vectorstore):
        RELEVANCE_THRESHOLD = 0.5
        relevant_docs = vectorstore.similarity_search_with_relevance_scores(question, k=5)
        has_relevant_docs = any(score > RELEVANCE_THRESHOLD for _, score in relevant_docs)

        return "vectorstore" if has_relevant_docs else "general"


    def setup_rag_chain(self, vectorstore):
   
        self.retail_template = PromptTemplate(
            template="""You are a knowledgeable retail business expert with deep insights into industry trends, best practices, customer behavior, supply chain management, and strategic planning. Your expertise enables you to provide actionable advice and innovative solutions to help retail businesses grow, optimize operations, and navigate market challenges successfully.
            Previous conversation:
            {chat_history}
            Current question: {question}
            If the question is outside the retail domain, acknowledge this first.
            Then provide a helpful response.
            Assistant:""",
            input_variables=["chat_history", "question"],
        )

        self.vectorstore_template = PromptTemplate(
            template="""You are a retail business expert using the following information to answer the question.
            Context:
            {context}

            Previous conversation:
            {chat_history}

            Current question: {input}

            Based on the context and your expertise, provide a detailed answer including:
            - Industry best practices
            - Current trends
            - Strategic recommendations
            - Potential challenges and solutions

            Assistant:""",
            input_variables=["context", "chat_history", "input"],
        )

        question_prompt = PromptTemplate(
            input_variables=["input", "chat_history"],
            template="""Given the conversation history and a follow-up question, rephrase the follow-up question to be a standalone question.

            Chat History:
            {chat_history}

            Follow-up question: {input}

            Standalone question:""",
        )

        history_aware_retriever = create_history_aware_retriever(
            llm=self.llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
            prompt=question_prompt
        )

        combine_docs_chain = create_stuff_documents_chain(
            llm=self.llm,
            prompt=self.vectorstore_template
        )

        rag_chain = create_retrieval_chain(
            retriever=history_aware_retriever,
            combine_docs_chain=combine_docs_chain
        )

       
        def enhanced_qa_chain(question: str):
            relevance = self.check_question_relevance(question, vectorstore)

            chat_history = self.memory.chat_memory.messages[-6:] if self.memory.chat_memory.messages else []
            history_str = "\n".join(
                [f"{msg.type}: {msg.content}" for msg in chat_history]
            )

            if relevance == "vectorstore":
                inputs = {
                    "input": question,
                    "chat_history": history_str
                }
                response = rag_chain.invoke(inputs)
                answer = response["answer"]
            else:
                prompt = self.retail_template.format(chat_history=history_str, question=question)
                answer = self.llm.invoke(prompt)
                self.memory.chat_memory.add_user_message(question)
                self.memory.chat_memory.add_ai_message(answer)

            self.save_conversation(question, answer)
            return {"result": answer}

        return enhanced_qa_chain


    def initialize_rag(self):
        vectorstore = self.setup_vectorstore()
        qa_chain = self.setup_rag_chain(vectorstore)
        return qa_chain

    def get_conversation_history(self) -> List[Dict]:
        return [{"type": msg.type, "content": msg.content} for msg in self.memory.chat_memory.messages]

    def clear_memory(self):
        self.memory.clear()