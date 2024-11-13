from sqlalchemy import Column, Integer, DateTime, Text, func, ForeignKey, UUID
from uuid_extensions import uuid7

from app.core.sql import engine

from .base import Base


class Chat(Base):
    __tablename__ = 'chats'

    id = Column(UUID, primary_key=True, default=uuid7())
    # user_id = Column(Integer, ForeignKey('user.id'))
    type = Column(Text)
    message = Column(Text)
    created_at = Column(DateTime, default=func.now())


# Base.metadata.create_all(engine)
