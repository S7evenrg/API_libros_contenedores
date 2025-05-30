from models import AuthorDB, BookDB
from database import Base, SessionLocal, engine
from schemas import AuthorModel, BookModel
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException

import logging


logging.basicConfig(
	level=logging.DEBUG, # DEBUG, INFO, WARNING, ERROR, CRITICAL
	format="%(asctime)s - %(name)s - %(levelname)s - %(message)s "
)

logger = logging.getLogger(__name__)


"""
def create_author(name: str) -> AuthorModel:
    if any(a.name == name for a in AuthorModel):
        raise ValueError("El autor ya existe")
    new_author = AuthorModel(id=len(AuthorModel)+1, name=name, bio=None)
    AuthorModel.append(new_author)
    return new_author
"""

def create_author(author: AuthorModel, db: Session ):
    """
    Crea un nuevo autor en la base de datos.
    """
    logger.debug(f"Intentando crear el autor: {author.name}")
    
    existing_author = db.query(AuthorDB).filter(AuthorDB.name == author.name).first()
    if existing_author:
        logger.error(f"El autor {author.name} ya existe.")
        
    
    db_author = AuthorDB(id=author.id, name=author.name, bio=author.bio)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    
    logger.info(f"Autor {db_author.name} creado exitosamente.")
    return db_author

def get_authors(db: Session):
    authors = db.query(AuthorDB).all()
    return authors


def create_book(title: str, author_id: int) -> BookModel:
    if not any(a.id == author_id for a in AuthorModel):
        raise ValueError("El autor no existe")
    new_book = BookModel(id=len(BookModel)+1, title=title, author_id=author_id)
    BookModel.append(new_book)
    return new_book

    """
def search_authors(name: str):
    return [author for author in authors if name.lower() in author.name.lower()]

def search_books(title: str):
    return [book for book in books if title.lower() in book.title.lower()]

def get_books_by_author(author_id: int, skip: int = 0, limit: int = 10):
    filtered_books = [book for book in books if book.author_id == author_id]
    return filtered_books[skip:skip + limit]

def get_books_by_author_name(author_id: int, skip: int = 0, limit: int = 10):
    filtered_books = [book for book in books if book.author_id == author_id]
    return filtered_books[skip:skip + limit]

def get_paginated_authors(skip: int = 0, limit: int = 10):
    return authors[skip:skip + limit]

def get_paginated_books(skip: int = 0, limit: int = 10):
    return books[skip:skip + limit]

"""