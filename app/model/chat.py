from sqlmodel import SQLModel, Field
from uuid import UUID
from uuid_extensions import uuid7
from datetime import datetime


class Chat(SQLModel, table=True):
    __tablename__ = 'chats'

    id: UUID = Field(default_factory=uuid7, primary_key=True)
    type: str
    message: str
    created_at: datetime = Field(default_factory=datetime.now)
