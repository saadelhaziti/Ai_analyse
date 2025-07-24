from typing import List
from fastapi import APIRouter, HTTPException

import chatbot.controllers.chatbot_controller as chatbot_controller
from chatbot.schemas.chat_schema import ChatMessage, ChatResponse, ConversationInfo, ConversationMessage, ConversationResponse

Chat = APIRouter()


@Chat.post("/chat/", response_model=ChatResponse)
async def create_chat(chat_message: ChatMessage):
    chat_response = await chatbot_controller.chat_controller(chat_message)
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
