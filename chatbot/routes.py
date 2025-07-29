from typing import List
from fastapi import APIRouter, HTTPException, Depends
import chatbot.controllers.chatbot_controller as chatbot_controller
from chatbot.schemas.chat_schema import ChatMessage, ChatResponse, ConversationInfo, ConversationMessage, ConversationResponse
from DB_Save.routes import get_db
from sqlalchemy.orm import Session
Chat = APIRouter()


@Chat.post("/chat/{guid_project}", response_model=ChatResponse)
async def create_chat(guid_project: str, chat_message: ChatMessage, db: Session = Depends(get_db)):
    chat_response = await chatbot_controller.chat_controller(chat_message, guid_project, db)
    if not chat_response:   
        raise HTTPException(status_code=400, detail="Chat creation failed")
    return chat_response


@Chat.get("/conversation/{conversation_id}", response_model=ConversationResponse)
async def get_conversation(conversation_id: str):   
    messages = await chatbot_controller.get_conversation_controller(conversation_id)
    if not messages:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return ConversationResponse(
            id=conversation_id,
            messages=[ConversationMessage(**msg) for msg in messages]
        )

@Chat.get("/conversation", response_model=List[ConversationInfo])
async def list_conversations():
    return await chatbot_controller.get_recent_conversations_controller()
