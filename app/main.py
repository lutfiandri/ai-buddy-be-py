import os

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langchain_openai import ChatOpenAI
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.sql import create_tables

from app import router

# Set environment variables
os.environ["OPENAI_API_KEY"] = settings.openai_api_key

# Initialize model
model = ChatOpenAI(model="gpt-4o-mini")


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


# FastAPI app instance
app = FastAPI(lifespan=lifespan)

app.include_router(router.chat_router)
app.include_router(router.auth_router)
