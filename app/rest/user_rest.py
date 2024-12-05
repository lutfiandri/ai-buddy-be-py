from pydantic import BaseModel


class CreateRequest(BaseModel):
    username: str
    password: str
