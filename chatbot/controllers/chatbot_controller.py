from http.client import HTTPException
from chatbot.schemas.chat_schema import ChatMessage
from chatbot.services import chatbot_services


async def chat_controller(chat_message: ChatMessage):
    if not chat_message:
        raise HTTPException(status_code=400, detail="Chat message is required")
    if not chat_message.question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    return await chatbot_services.create_chat(chat_message)

async def get_conversation_controller(conversation_id: str):
    if not conversation_id:
        raise HTTPException(status_code=400, detail="Conversation ID is required")
    
    return await chatbot_services.get_conversation(conversation_id)

async def get_recent_conversations_controller():
    return await chatbot_services.get_recent_conversations()
   
    