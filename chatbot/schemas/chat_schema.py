from typing import List, Optional
from pydantic import BaseModel


class ChatMessage(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    guid_project: str
    timestamp: str


class ConversationMessage(BaseModel):
    timestamp: str
    question: str
    answer: str

class ConversationInfo(BaseModel):
    id: str
    started: str
    first_question: str
    message_count: int

class ConversationResponse(BaseModel):
    id: str
    messages: List[ConversationMessage]