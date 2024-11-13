import json

from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.dependency import db_session
from app.rest import chat_rest
from app.model import Chat

router = APIRouter()


@router.post("/sessions/{session_id}/chats")
async def create_chat(session_id: str, req: chat_rest.CreateRequest, db_session=Depends(db_session)):
    new_chat = Chat(type="human", message=req.chat)
    db_session.add(new_chat)
    await db_session.commit()
    return {
        "session_id": session_id,
        "req": req
    }
