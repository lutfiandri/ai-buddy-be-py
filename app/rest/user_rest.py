from pydantic import BaseModel
from typing import overload

from app.model import User


class UserResponse(BaseModel):
    id: str
    username: str

    @classmethod
    def from_model(cls, user: User):
        return cls(id=user.id.hex, username=user.username)


class CreateUserRequest(BaseModel):
    username: str
    password: str
