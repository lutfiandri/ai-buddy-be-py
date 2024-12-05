from pydantic import BaseModel


class ChatResponse(BaseModel):
    session_id: str
    chat: str


class CreateChatRequest(BaseModel):
    chat: str
