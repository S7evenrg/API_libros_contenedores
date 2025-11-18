from pydantic import BaseModel
from typing import Optional, List


class BookModel(BaseModel):
    id: Optional[int] = None
    title: str
    published_date: Optional[str] = None
    summary: Optional[str] = None
    author_id: int

    class Config:
        from_attributes = True


class AuthorModel(BaseModel):
    id: Optional[int] = None
    name: str
    bio: Optional[str] = None
    books: Optional[List[BookModel]] = None

    class Config:
        from_attributes = True
