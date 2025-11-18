from app.db.models import AuthorDB, BookDB
from app.db.database import Base, SessionLocal, engine
from app.schemas.schemas import AuthorModel, BookModel
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException

import logging


logging.basicConfig(
    level=logging.DEBUG, # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s "
)

logger = logging.getLogger(__name__)


def create_author(author: AuthorModel, db: Session ):
    """ Crea un nuevo autor en la base de datos.  """
    logger.debug(f"Intentando crear el autor: {author.name}")
    
    existing_author = db.query(AuthorDB).filter(AuthorDB.name == author.name).first()
    if existing_author:
        logger.error(f"El autor {author.name} ya existe.")
        raise HTTPException(status_code=400, detail="El autor ya existe")

    # id (auto-incremental).
    db_author = AuthorDB(name=author.name, bio=author.bio)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    
    logger.info(f"Autor {db_author.name} creado exitosamente.")
    return db_author

def get_authors(db: Session):
    authors = db.query(AuthorDB).all()
    return authors


def create_book(book: BookModel, db: Session) -> BookModel:
    """ Crea un libro en la base de datos usando el esquema 'BookModel'. """
    logger.debug(f"Intentando crear el libro: {book.title}")

    # Verificar que el autor exista
    author = db.query(AuthorDB).filter(AuthorDB.id == book.author_id).first()
    if not author:
        logger.error(f"El autor con id {book.author_id} no existe.")
        raise HTTPException(status_code=400, detail="El autor no existe")

    db_book = BookDB(
        title=book.title,
        author_id=book.author_id,
        summary=book.summary,
    )

    # Parsear published_date si viene en formato dd/mm/YYYY
    if book.published_date:
        try:
            from datetime import datetime
            db_book.published_date = datetime.strptime(book.published_date, "%d/%m/%Y").date()
        except Exception:
            logger.warning(f"No se pudo parsear published_date: {book.published_date}")

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    logger.info(f"Libro '{db_book.title}' creado correctamente con id {db_book.id}")
    return db_book

def get_books(db: Session):
    books = db.query(BookDB).all()
    return books

def search_authors(name: str, db: Session):
    """ Busca autores cuyo nombre contenga 'name' (case-insensitive)."""
    if not name:
        return []
    return db.query(AuthorDB).filter(AuthorDB.name.ilike(f"%{name}%")).all()


def search_books(title: str, db: Session):
    """ Busca libros cuyo título contenga 'title' (case-insensitive)."""
    if not title:
        return []
    return db.query(BookDB).filter(BookDB.title.ilike(f"%{title}%")).all()
