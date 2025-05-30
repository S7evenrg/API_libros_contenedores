
from pydantic import BaseModel
from typing import Optional, List

class BookModel(BaseModel):
    id: int
    title: str
    published_date: Optional[str] = None
    summary: Optional[str] = None    
    author_id: int

    class Config:
        from_attributes = True

class AuthorModel(BaseModel):
    id: int
    name: str
    bio: Optional[str] = None
    books: Optional[List[BookModel]] = []

    class Config:
        from_attributes = True
