import asyncio
from chatbot.schemas.chat_schema import ChatMessage
from chatbot.services.chat_manager import ChatManager


chat_manager = ChatManager()


async def create_chat(chat_message: ChatMessage):
    return await chat_manager.process_message(chat_message.question, chat_message.conversation_id)

async def get_conversation(conversation_id: str):
    return await chat_manager.get_conversation(conversation_id)

async def get_recent_conversations():
    return await chat_manager.get_recent_conversations()