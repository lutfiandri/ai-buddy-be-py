from pydantic import BaseModel


class CreateRequest(BaseModel):
    chat: str
