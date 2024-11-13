from app.core.sql import async_session
from sqlalchemy.ext.asyncio import AsyncSession


async def db_session() -> AsyncSession:
    async with async_session() as session:
        yield session
