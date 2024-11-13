from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

from .config import settings


# Database URL for asyncpg
DATABASE_URL = f"postgresql+asyncpg://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"

print(DATABASE_URL)

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session maker
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
