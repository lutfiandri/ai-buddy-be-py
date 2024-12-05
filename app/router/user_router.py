import json

from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.dependency import Session, db_session
from app.rest.user_rest import *
from app.model import User

router = APIRouter()


@router.post("/users")
async def create_chat(req: CreateRequest, db: Session = Depends(db_session)):
    # new_user = User()
    # db_session.add(new_chat)
    # await db_session.commit()
    return req
