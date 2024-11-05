import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from psycopg_pool import ConnectionPool
from langchain_openai import ChatOpenAI
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.langchain import chat_to_ai
from app.rest.chat import CreateChatRequest

# Set environment variables
os.environ["OPENAI_API_KEY"] = settings.openai_api_key

# Initialize model
model = ChatOpenAI(model="gpt-4o-mini")

# FastAPI app instance
app = FastAPI()

# Database connection information
conn_info = f"host={settings.database_host} port={settings.database_port} dbname={settings.database_name} user={settings.database_user} password={settings.database_password}"

# Initialize ConnectionPool, but don't connect immediately
pool = ConnectionPool(conn_info)

# Startup event to initialize the pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    pool.open()  # Open the pool to start making connections available
    print("Database connection pool initialized")
    yield
    pool.close()  # Properly close the pool when the app shuts down
    print("Database connection pool closed")


def get_db_connection():
    with pool.connection() as conn:
        yield conn


@app.post("/sessions/{session_id}/chats")
def create_chat(session_id: str, req: CreateChatRequest, conn=Depends(get_db_connection)):
    try:
        response = chat_to_ai(chat=req.chat, conn=conn,
                              model=model, session_id=session_id)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Error in processing the request")
