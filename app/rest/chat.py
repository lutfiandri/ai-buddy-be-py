from pydantic import BaseModel


class CreateChatRequest(BaseModel):
    chat: str
