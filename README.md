# API de Libros y Autores

## Características
- FastAPI con POO
- Autenticación HTTP Basic
- Validación de datos
- Control de errores HTTP
- Búsqueda de autores y libros
- Paginación y filtrado por autor

## Endpoints
- POST /authors
- GET /authors
- POST /books
- GET /books
- GET /search/authors?name=...
- GET /search/books?title=...
- GET /books/by_author/{author_id}
- GET /authors/paginated?skip=0&limit=10
- GET /books/paginated?skip=0&limit=10

## Uso
```bash
uvicorn main:app --reload
```

Usuario: admin  
Contraseña: password123