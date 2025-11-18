from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.db import crud
from app.auth.auth import verify_credentials

import logging

from sqlalchemy.orm import Session
from app.db.database import SessionLocal, engine, Base, get_db
from app.db.models import AuthorDB, BookDB
from app.schemas.schemas import AuthorModel, BookModel

from app.db.init_db import init, check_and_create_tables

init()  # Inicializar la base de datos

logging.basicConfig(
    level=logging.DEBUG, # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s "
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Mi Primera API trabajo Final Modulo de Programacion Avanzada",
    description="Una API para trabajo final del modulo Programcion Avanzada",
    version="10.0.1"
)


@app.get("/")
def initial_greating():
    logger.debug(f"metodo get de la ruta // probando el get inicial")
    logger.info(f"metodo get de la ruta // saludos")
    logger.warning("metodo get de la ruta // sin autenticacion")

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

@app.get("/authors/")
async def list_authors(db : Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return crud.get_authors(db)

@app.post("/books", response_model=BookModel)
async def add_book(book: BookModel, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return crud.create_book(book, db)

@app.get("/books")
async def list_books(db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return crud.get_books(db)


@app.get("/search/authors")
async def search_authors(name: str, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    """Buscar autores por nombre (query param `name`)."""
    return crud.search_authors(name, db)


@app.get("/search/books")
async def search_books(title: str, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    """Buscar libros por título (query param `title`)."""
    return crud.search_books(title, db)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content={"message": "Error de validación", "errors": exc.errors()})
