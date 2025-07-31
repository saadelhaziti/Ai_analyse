import asyncio
from chatbot.schemas.chat_schema import ChatMessage
from chatbot.services.chat_manager import ChatManager
from sqlalchemy.orm import Session
from DB_Save.routes import get_db
from fastapi import Depends

chat_manager = ChatManager()


async def create_chat(chat_message: ChatMessage, guid_project: str, db: Session = Depends(get_db)):
    return await chat_manager.process_message(chat_message.question, guid_project, db)

async def get_conversation(guid_project: str, db: Session = Depends(get_db)):
    return await chat_manager.get_conversation(guid_project, db)

async def get_recent_conversations():
    return await chat_manager.get_recent_conversations()