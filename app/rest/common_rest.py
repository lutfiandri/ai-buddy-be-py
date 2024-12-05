from pydantic import BaseModel
from typing import TypeVar, Generic, List

T = TypeVar('T')


class Response(BaseModel, Generic[T]):
    status: str = 'success'
    data: T


class PageResponse(BaseModel, Generic[T]):
    status: str = 'success'
    data: List[T]
