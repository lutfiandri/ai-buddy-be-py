import json

from fastapi import APIRouter, Depends, HTTPException, status

from app.dependency import db_session, Session
from app.rest.common_rest import *
from app.rest.chat_rest import *
from app.model import Chat

router = APIRouter()


@router.post("/sessions/{session_id}/chats", response_model=Response[ChatResponse])
async def create_chat(session_id: str, req: CreateChatRequest, db: Session = Depends(db_session)):
    # if session_id == '*':

    new_chat = Chat(type="human", message=req.chat)
    db.add(new_chat)
    db.commit()

    response = Response(status='created', data=ChatResponse(chat=new_chat.message))
    return response
