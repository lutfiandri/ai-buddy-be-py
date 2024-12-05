from sqlmodel import SQLModel, Field
from uuid import UUID
from uuid_extensions import uuid7
from datetime import datetime


class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: UUID = Field(default_factory=uuid7, primary_key=True)
    username: str = Field(nullable=False, unique=True)
    password: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
