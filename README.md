# API de Libros y Autores

## Características

- FastAPI con POO
- Autenticación HTTP Basic
- Validación de datos
- Control de errores HTTP
- Búsqueda de autores y libros **NO**
- Paginación y filtrado por autor  **NO**

## Endpoints

- POST /authors   **SI**
- GET /authors     **SI**
- POST /books	  **SI**
- GET /books       **SI**
- GET /search/authors?name=...   **NO**
- GET /search/books?title=...         **NO**
- GET /books/by_author/{author_id}      **NO**
- GET /authors/paginated?skip=0&limit=10    **NO**
- GET /books/paginated?skip=0&limit=10       **NO**

## Archivos

| Archivo                | Descripción                                                                              |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| [create_all_tables.py] | Script para crear todas las tablas en la base de datos usando SQLAlchemy.                 |
| [crud.py]              | Funciones CRUD (Crear, Leer, Actualizar, Eliminar) para interactuar con la base de datos. |
| [database.py]          | Configuración de la conexión a la base de datos y la instancia de SQLAlchemy.           |
| [drop_all_tables.py]   | Script para eliminar todas las tablas de la base de datos.                                |
| [drop_db.py]           | Script para eliminar la base de datos completa o su contenido.                            |
| [init_db.py]           | Inicializa la base de datos, creando tablas.                                             |
| [main.py]              | Archivo principal de la API, contiene la configuración de FastAPI.                      |
| [models.py]            | Definición de los modelos de datos (tablas) usando SQLAlchemy.                           |
| [request.py]           | Funciones para manejar peticiones HTTP y/o interacciones externas.                        |
| [schemas.py]           | Definición de los esquemas Pydantic para validación y serialización de datos.          |
| [seed_tables.py]       | Script para poblar la base de datos con datos de ejemplo.                                 |
| [test_api.py]          | Pruebas automatizadas para la API, usando frameworks como pytest.                         |

## Uso

```bash
uvicorn main:app --reload
```

Usuario: admin
Contraseña: password123

## Video

[Ejecucion API](Ejecucion API)
