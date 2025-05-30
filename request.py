import requests
from requests.auth import HTTPBasicAuth

# URL de tu API (ajústala si está corriendo en otra dirección o puerto)
url = "http://127.0.0.1:8000/authors/"

# Datos del autor
# payload 
author = {
    "id" : 77,
    "name" : "Javier Fabian",
    "bio" : "Escritor europeo, autor de Ray1uela."
}

# Hacer la solicitud con autenticación básica
response = requests.post(url, json=author, auth=HTTPBasicAuth("admin", "password123"))
response_all_authors = requests.get(url, auth=HTTPBasicAuth("admin", "password123"))

print(response)
# Mostrar resultado
print("Código de estado_POST:", response.status_code)
print("Respuesta:", response.json())


print("Código de estado_GET:", response_all_authors.status_code)
print("Respuesta:", response_all_authors.json())

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
