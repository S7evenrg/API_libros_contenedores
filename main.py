from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.exceptions import HTTPException as StarletteHTTPException
import crud 

#from database import books
from auth import verify_credentials

import logging

from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base, get_db
from models import AuthorDB, BookDB
from schemas import AuthorModel, BookModel
#from fastapi.middleware.cors import CORSMiddleware

from init_db import init, check_and_create_tables

# Crear las tablas
#Base.metadata.create_all(bind=engine)

init()  # Inicializar la base de datos

#check_and_create_tables()  # Verificar y crear tablas si no existen

# Crear las tablas de Author y Book
#Author.Base.metadata.create_all(bind=engine)
#Book.Base.metadata.create_all(bind=engine)

logging.basicConfig(
	level=logging.DEBUG, # DEBUG, INFO, WARNING, ERROR, CRITICAL
	format="%(asctime)s - %(name)s - %(levelname)s - %(message)s "
)

logger = logging.getLogger(__name__)

app = FastAPI(
	title="Mi Primera API trabajo Final Modulo de Programacion Avanzada",
	description="UNA API para trabajo final del modulo",
	version="10.0.1"
)
"""
logger.debug(f"metodo get de la ruta /")
logger.info(f"")
logger.warning("")
"""




@app.get("/")
def initial_greating():
    logger.debug(f"metodo get de la ruta // probando el get inicial")
    logger.info(f"metodo get de la ruta // saludos")
    #logger.warning("metodo get de la ruta // sin autenticacion")

    return {"message": "Bienvenido a la API de gestión de libros y autores. " +
    "Si quieres ver mas info al respecto debes autenticarte. " +
    "Puedes probar con el usuario 'admin' y la contraseña 'password123'. " +
    "Solicita tus credenciales con el administrador del sistema."}

@app.post("/authors/", response_model=AuthorModel)
def add_author(author: AuthorModel, db : Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(verify_credentials)):

    logger.debug(f"metodo post de la ruta {author} //authors probando inserts iniciales")
    logger.info(f"metodo post de la ruta {db}//authors lista generada")

    try:
        return crud.create_author(author, db)
    except HTTPException as e:
        logger.error(f"Error al crear el autor: {e.detail}")
        raise HTTPException(status_code=400, detail="El autor ya existe")

#async 

#@app.post("/authors/", response_model=AuthorModel)
@app.get("/authors/")
async def list_authors(db : Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return crud.get_authors(db)
"""
@app.post("/books")
async def add_book(book: BookCreate, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return crud.create_book(book.title, book.author_id)

@app.get("/books")
async def list_books(credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return books

@app.get("/search/authors")
async def search_authors(name: str, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return crud.search_authors(name)

@app.get("/search/books")
async def search_books(title: str, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return crud.search_books(title)

@app.get("/books/by_author/{author_id}")
async def get_books_by_author(author_id: int, skip: int = 0, limit: int = 10, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return crud.get_books_by_author(author_id, skip, limit)

@app.get("/books/by_author_name/{author_name}")
async def get_books_by_author_name(author_name: str, limit: str = 10, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return crud.get_books_by_author(author_name, limit)

@app.get("/authors/paginated")
async def paginated_authors(skip: int = 0, limit: int = 10, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return crud.get_paginated_authors(skip, limit)

@app.get("/books/paginated")
async def paginated_books(skip: int = 0, limit: int = 10, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return crud.get_paginated_books(skip, limit)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content={"message": "Error de validación", "errors": exc.errors()})
"""