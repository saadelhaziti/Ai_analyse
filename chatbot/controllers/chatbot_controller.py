from chatbot.schemas.chat_schema import ChatMessage
from chatbot.services import chatbot_services
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from DB_Save.routes import get_db


async def chat_controller(chat_message: ChatMessage, guid_project: str, db: Session = Depends(get_db)):
    if not chat_message:
        raise HTTPException(status_code=400, detail="Chat message is required")
    if not chat_message.question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    return await chatbot_services.create_chat(chat_message, guid_project, db)

async def get_conversation_controller(guid_project: str, db: Session = Depends(get_db)):
    if not guid_project:
        raise HTTPException(status_code=400, detail="Conversation ID is required")
    
    return await chatbot_services.get_conversation(guid_project, db)

async def get_recent_conversations_controller():
    return await chatbot_services.get_recent_conversations()
   
    