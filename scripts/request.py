import requests
from requests.auth import HTTPBasicAuth

# URL de tu API (ajústala si está corriendo en otra dirección o puerto)
url = "http://127.0.0.1:8000/authors/"

# Datos del autor
author = {
    "name" : "Gema Bosh",
    "bio" : "Escritora nueva, autor de libros de arte lalanda."
}

# Hacer la solicitud con autenticación básica
response = requests.post(url, json=author, auth=HTTPBasicAuth("admin", "password123"))
response_all_authors = requests.get(url, auth=HTTPBasicAuth("admin", "password123"))

print(response)
# Mostrar resultado
print("Código de estado_POST:", response.status_code)
try:
    print("Respuesta:", response.json())
except Exception:
    print("Respuesta no es JSON:", response.text)


print("Código de estado_GET:", response_all_authors.status_code)
try:
    print("Respuesta:", response_all_authors.json())
except Exception:
    print("Respuesta no es JSON:", response_all_authors.text)

# Verificar si la solicitud fue exitosa
if response.status_code == 200 or response.status_code == 201:
    print("Autor creado exitosamente.") 
else:
    print("Error al crear el autor:", response.text)
# Verificar si la solicitud fue exitosa
if response_all_authors.status_code == 200:
    print("Autores obtenidos exitosamente.")    
else:
    print("Error al obtener los autores:", response_all_authors.text)
# Mostrar todos los autores
print("Autores:", response_all_authors.json())

# --- Crear un libro asociado al autor creado (si la creación del autor fue exitosa) ---
book_url = "http://127.0.0.1:8000/books"

if response.status_code in (200, 201):
    try:
        created_author = response.json()
        # Obtener el id del autor retornado por la API (si existe)
        author_id = created_author.get("id") if isinstance(created_author, dict) else None
    except Exception:
        author_id = None

    if author_id:
        book = {
            "title": "Mi valencia de hoy",
            "author_id": author_id,
            "published_date": "01/10/2025",
            "summary": "Resumen de ejemplo libro de autora valenciana"
        }

        response_book = requests.post(book_url, json=book, auth=HTTPBasicAuth("admin", "password123"))
        print("Código de estado_POST book:", response_book.status_code)
        try:
            print("Respuesta book:", response_book.json())
        except Exception:
            print("Respuesta book no es JSON:", response_book.text)

        # Obtener todos los libros
        response_all_books = requests.get(book_url, auth=HTTPBasicAuth("admin", "password123"))
        print("Código de estado_GET books:", response_all_books.status_code)
        try:
            print("Libros:", response_all_books.json())
        except Exception:
            print("Respuesta books no es JSON:", response_all_books.text)
    else:
        print("No se pudo obtener el `id` del autor creado; no se creó el libro.")
else:
    print("No se creó el autor, no se intentará crear libro.")
