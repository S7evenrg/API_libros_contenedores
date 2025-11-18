from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido a la API de gestión de libros y autores. " +
    "Si quieres ver mas info al respecto debes autenticarte. " +
    "Puedes probar con el usuario 'admin' y la contraseña 'password123'. " +
    "Solicita tus credenciales con el administrador del sistema."}

def test_create_author():
    response = client.post(
        "/authors",
        json={"id":5550,"name": "Eduard Gamez", "bio": "peruan author"},
        auth=("admin", "password123")
    )
    assert response.status_code == 200