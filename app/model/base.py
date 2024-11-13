from sqlalchemy.orm import declarative_base

from app.core.sql import engine

Base = declarative_base()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Tables created")
