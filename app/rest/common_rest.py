from pydantic import BaseModel
from typing import TypeVar, Generic, List
from fastapi import HTTPException

T = TypeVar('T')


class Response(BaseModel, Generic[T]):
    data: T


class PageResponse(BaseModel, Generic[T]):
    data: List[T]
