from sqlmodel import create_engine, SQLModel

from .config import settings

DATABASE_URL = f"postgresql+psycopg://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"

print(DATABASE_URL)

engine = create_engine(DATABASE_URL, echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine)
