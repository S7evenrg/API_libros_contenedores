from sqlalchemy import Column, Integer, String, Text, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class AuthorDB(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    bio = Column(Text, nullable=True)
    books = relationship("BookDB", back_populates="author")

    
    def __init__(self, id: int, name: str, bio: str, books: list = None):
        self.id = id
        self.name = name
        self.bio = bio
        self.books = []
    

class BookDB(Base):
    __tablename__ = "   books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    summary = Column(Text, nullable=True)
    published_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    author = relationship("AuthorDB", back_populates="books")

    def __init__(self, id: int, title: str, author_id: int, published_date: str = None, summary: str = None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.published_date = datetime.strptime(published_date, "%d/%m/%Y") if published_date else None
        self.summary = None
