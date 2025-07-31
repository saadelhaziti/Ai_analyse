import json
from typing import Dict, List, Optional
import asyncio
from datetime import datetime
from chatbot.schemas.chat_schema import ChatResponse
from chatbot.services.retail_rag import RetailRAG
from sqlalchemy.orm import Session
from DB_Save.routes import get_db
from users.services.Project_Services import get_project
from DB_Save.controller.Minio_controller import Get_file_from_minio
from fastapi import Depends


class ChatManager:
    def __init__(self):
        self.rag = RetailRAG()
        self.qa_chain = None

    async def initialize(self):
        """Initialize the RAG system"""
        # Run initialization in a thread pool to avoid blocking
        self.qa_chain = await asyncio.get_event_loop().run_in_executor(
            None, self.rag.initialize_rag
        )

    async def process_message(
        self, question: str, guid_project: str, db: Session = Depends(get_db)
    ) -> Dict:
        """Process a chat message"""
        # Load existing conversation if ID provided
        self.rag.set_conversation_id(guid_project, db)
        self.rag.load_existing_conversation()

        # Get response from RAG system (run in thread pool)
        response = await asyncio.get_event_loop().run_in_executor(
            None, self.qa_chain, question
        )

        timestamp = datetime.now().isoformat()

        return ChatResponse(
            answer=response["result"],
            guid_project=self.rag.guid_project,
            timestamp=timestamp,
        )

    async def get_recent_conversations(self) -> List[Dict]:
        """Get list of recent conversations"""
        conversations = self.rag.load_conversation_history()
        conv_list = []

        for conv_id, messages in conversations.items():
            if messages:
                conv_list.append(
                    {
                        "id": conv_id,
                        "started": messages[0]["timestamp"],
                        "first_question": messages[0]["question"],
                        "message_count": len(messages),
                    }
                )


        conv_list.sort(key=lambda x: x["started"], reverse=True)
        return conv_list[:5] 

    async def get_conversation(self, guid_project: str, db: Session = Depends(get_db)) -> Optional[Dict]:
        """Get a specific conversation history"""
        proj = get_project(db, guid_project)
        user_id = str(proj.guid_user)
        key_path = f"{user_id}/{guid_project}/conversations.json"
      
        try:
            file_stream, _ = Get_file_from_minio(key_path)

            if file_stream:
                conversations = file_stream.read().decode('utf-8')
                return json.loads(conversations)
        except FileNotFoundError:
            return None
                

