import json

from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.dependency import db_session, Session
from app.rest import chat_rest
from app.model import Chat

router = APIRouter()


@router.post("/sessions/{session_id}/chats")
async def create_chat(session_id: str, req: chat_rest.CreateRequest, db: Session = Depends(db_session)):
    new_chat = Chat(type="human", message=req.chat)
    db.add(new_chat)
    db.commit()
    return new_chat
