import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_huggingface import HuggingFaceEmbeddings


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
        self.current_conversation_id = None
        self.set_new_conversation_id()

    def list_conversations(self) -> List[str]:
        if os.path.exists(self.conversation_store):
            with open(self.conversation_store, "r") as f:
                conversations = json.load(f)
            return list(conversations.keys())
        return []

    def set_new_conversation_id(self):
        self.clear_memory()
        self.current_conversation_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    def set_conversation_id(self, conversation_id: str):
        self.current_conversation_id = conversation_id

    def load_conversation_history(self) -> Dict:
        if os.path.exists(self.conversation_store):
            with open(self.conversation_store, "r") as f:
                return json.load(f)
        return {}

    def load_existing_conversation(self, conversation_id: str) -> bool:
        conversations = self.load_conversation_history()
        if conversation_id in conversations:
            self.set_conversation_id(conversation_id)
            for exchange in conversations[conversation_id]:
                if "question" in exchange and "answer" in exchange:
                    self.memory.chat_memory.add_user_message(exchange["question"])
                    self.memory.chat_memory.add_ai_message(exchange["answer"])
            return True
        return False

    def save_conversation(self, question: str, answer: str):
        conversations = self.load_conversation_history()
        if self.current_conversation_id not in conversations:
            conversations[self.current_conversation_id] = []
        conversations[self.current_conversation_id].append(
            {
                "timestamp": datetime.now().isoformat(),
                "question": question,
                "answer": answer,
            }
        )
        with open(self.conversation_store, "w") as f:
            json.dump(conversations, f, indent=2)

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

        if not has_relevant_docs:
            system_prompt = """You are a retail business expert. Determine if this question is related to:
            - Retail business operations
            - Consumer behavior
            - Market trends
            - Store operations
            - E-commerce
            - Retail technology
            - Supply chain and inventory
            - Retail marketing
            - Customer experience
            Respond only with 'true' if related to any of these areas, or 'false' if not."""

            response = self.llm.invoke(
                f"{system_prompt}\n\nQuestion: {question}\nAnswer (true/false):"
            )
            is_retail = response.strip().lower() == "true"
            return "retail" if is_retail else "general"

        return "vectorstore"

    def setup_rag_chain(self, vectorstore):
        retail_template = PromptTemplate(
            template="""You are a retail business expert.
            Previous conversation:
            {chat_history}
            Current question: {question}
            Please provide expert analysis based on retail industry knowledge, including:
            - Industry best practices
            - Current trends
            - Strategic recommendations
            - Potential challenges and solutions
            Assistant:""",
            input_variables=["chat_history", "question"],
        )

        general_template = PromptTemplate(
            template="""You are an AI designed for retail business analysis.
            Previous conversation:
            {chat_history}
            Current question: {question}
            If the question is outside the retail domain, acknowledge this first.
            Then provide a helpful response.
            Assistant:""",
            input_variables=["chat_history", "question"],
        )

        vectorstore_qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
            memory=self.memory,
            return_source_documents=True,
            verbose=False,
        )

        def enhanced_qa_chain(question):
            relevance = self.check_question_relevance(question, vectorstore)

            history_str = "\n".join(
                [f"{msg.type}: {msg.content}" for msg in self.memory.chat_memory.messages[-6:]]
            ) if self.memory.chat_memory.messages else ""

            if relevance == "vectorstore":
                response = vectorstore_qa_chain({"question": question})
                answer = response["answer"]

            elif relevance == "retail":
                prompt = retail_template.format(chat_history=history_str, question=question)
                answer = self.llm.invoke(prompt)
                self.memory.chat_memory.add_user_message(question)
                self.memory.chat_memory.add_ai_message(answer)

            else:
                prompt = general_template.format(chat_history=history_str, question=question)
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

    def save_final_conversation(self):
        conversations = self.load_conversation_history()
        if self.current_conversation_id in conversations:
            with open(self.conversation_store, "w") as f:
                json.dump(conversations, f, indent=2)
