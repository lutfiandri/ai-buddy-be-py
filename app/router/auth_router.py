from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlmodel import select

from app.dependency import Session, db_session
from app.rest import *
from app.model import User
from app.util.password import hash_password, compare_passwords

router = APIRouter()


@router.post("/auth/register", status_code=201, response_model=Response[UserResponse])
async def create(req: CreateUserRequest, db: Session = Depends(db_session)):
    try:
        hashed_password = hash_password(req.password)
        user = User(
            username=req.username,
            password=hashed_password,
        )

        db.add(user)
        db.commit()

        response = Response(data=UserResponse.from_model(user))

        return response

    except Exception as e:
        db.rollback()
        if "duplicate key value" in str(e).lower():
            raise HTTPException(status_code=409, detail="Username already exists")

        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/auth/login", status_code=200)
async def login(req: LoginRequest, db: Session = Depends(db_session)):
    try:
        statement = select(User).where(User.username == req.username)
        user = db.exec(statement).first()

        if user is None:
            raise HTTPException(status_code=401, detail="Invalid username or password")

        if not compare_passwords(req.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid username or password")

        return UserResponse.from_model(user)

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
