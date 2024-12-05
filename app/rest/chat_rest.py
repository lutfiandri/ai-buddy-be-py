from pydantic import BaseModel


class ChatResponse(BaseModel):
    chat: str


class CreateChatRequest(BaseModel):
    chat: str
