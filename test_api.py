from fastapi.testclient import TestClient
from main import app

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
        json={"id":121244211011,"name": "Gabruiel Garcías Márquez1f", "bio": "Colombian author"},
        auth=("admin", "password123")
    )
    assert response.status_code == 200
    #assert response.json()["msg"] == "AUTOR REGISTRADO"
    #assert response.json()["author"]["name"] == "Gabruiel Garcías Márquez1f"
"""
def test_list_authors():
    response = client.get("/authors", auth=("admin", "password123"))
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Assuming at least one author exists    

def test_create_book():
    response = client.post(
        "/books",
        json={"title": "Cien años de soledad", "author_id": 1},
        auth=("admin", "password123")
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Cien años de soledad"   

def test_list_books():
    response = client.get("/books", auth=("admin", "password123"))
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Assuming at least one book exists   

def test_search_authors():
    response = client.get(
        "/search/authors",
        params={"name": "Gabriel"},auth=("admin", "password123")
    )
    assert response.status_code == 200      

    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Assuming at least one author matches the search      
def test_search_books():    
    response = client.get(
        "/search/books",
        params={"title": "Cien años de soledad"},auth=("admin", "password123")      
    )
    assert response.status_code == 200  
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Assuming at least one book matches the search
def test_get_books_by_author():
    response = client.get(
        "/books/by_author/1",
        params={"skip": 0, "limit": 10}, auth=("admin", "password123")
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Assuming at least one book by the author exists  

def test_get_books_by_author_name():
    response = client.get(
        "/books/by_author_name/Gabriel García Márquez",
        params={"limit": 10}, auth=("admin", "password123")
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Assuming at least one book by the author exists  
def test_paginated_authors():
    response = client.get(
        "/authors/paginated",
        params={"skip": 0, "limit": 10}, auth=("admin", "password123")
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Assuming at least one author exists  
def test_paginated_books():
    response = client.get(
        "/books/paginated",
        params={"skip": 0, "limit": 10}, auth=("admin", "password123")
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0  # Assuming at least one book exists
def test_http_exception_handler():
    response = client.get("/non_existent_route", auth=("admin", "password123"))
    assert response.status_code == 404
    assert response.json() == {"message": "Not Found"}  # Assuming the handler returns this message 

def test_unauthorized_access():
    response = client.get("/authors")
    assert response.status_code == 401  # Unauthorized access without credentials
    assert response.json() == {"detail": "Not authenticated"}  # Assuming this is the default message for unauthenticated requests  
def test_invalid_credentials():
    response = client.get("/authors", auth=("wrong_user", "wrong_pass"))
    assert response.status_code == 401  # Unauthorized access with invalid credentials
    assert response.json() == {"detail": "Credenciales incorrectas"}  # Assuming this is the message for invalid credentials    
def test_create_author_unauthorized():
    response = client.post(
        "/authors",
        json={"name": "Unauthorized Author", "bio": "This should not be allowed"},
    )
    assert response.status_code == 401  # Unauthorized access without credentials
    assert response.json() == {"detail": "Not authenticated"}  # Assuming this is the default message for unauthenticated requests  
def test_create_book_unauthorized():
    response = client.post(
        "/books",
        json={"title": "Unauthorized Book", "author_id": 1},
    )
    assert response.status_code == 401  # Unauthorized access without credentials
    assert response.json() == {"detail": "Not authenticated"}  # Assuming this is the default message for unauthenticated requests
def test_list_authors_unauthorized():
    response = client.get("/authors")
    assert response.status_code == 401  # Unauthorized access without credentials
    assert response.json() == {"detail": "Not authenticated"}  # Assuming this is the default message for unauthenticated requests
def test_list_books_unauthorized():
    response = client.get("/books")
    assert response.status_code == 401  # Unauthorized access without credentials
    assert response.json() == {"detail": "Not authenticated"}  # Assuming this is the default message for unauthenticated requests  
def test_search_authors_unauthorized():
    response = client.get("/search/authors", params={"name": "Gabriel"})
    assert response.status_code == 401  # Unauthorized access without credentials
    assert response.json() == {"detail": "Not authenticated"}  # Assuming this is the default message for unauthenticated requests
def test_search_books_unauthorized():
    response = client.get("/search/books", params={"title": "Cien años de soledad"})
    assert response.status_code == 401  # Unauthorized access without credentials
    assert response.json() == {"detail": "Not authenticated"}  # Assuming this is the default message for unauthenticated requests
def test_get_books_by_author_unauthorized():
    response = client.get("/books/by_author/1", params={"skip": 0, "limit": 10})
    assert response.status_code == 401  # Unauthorized access without credentials
    assert response.json() == {"detail": "Not authenticated"}  # Assuming this is the default message for unauthenticated requests
def test_get_books_by_author_name_unauthorized():
    response = client.get("/books/by_author_name/Gabriel García Márquez", params={"limit": 10})
    assert response.status_code == 401  # Unauthorized access without credentials
    assert response.json() == {"detail": "Not authenticated"}  # Assuming this is the default message for unauthenticated requests
def test_paginated_authors_unauthorized():
    response = client.get("/authors/paginated", params={"skip": 0, "limit": 10})
    assert response.status_code == 401  # Unauthorized access without credentials
    assert response.json() == {"detail": "Not authenticated"}  # Assuming this is the default message for unauthenticated requests  
def test_paginated_books_unauthorized():
    response = client.get("/books/paginated", params={"skip": 0, "limit": 10})
    assert response.status_code == 401  # Unauthorized access without credentials
    assert response.json() == {"detail": "Not authenticated"}  # Assuming this is the default message for unauthenticated requests  
def test_create_author_invalid_data():
    response = client.post(
        "/authors",
        json={"name": "", "bio": "This should fail due to empty name"},
        auth=("admin", "password123")
    )
    assert response.status_code == 422  # Unprocessable Entity for validation errors
    assert "name" in response.json()["detail"][0]["loc"]  # Check if the error is related to the 'name' field
    assert response.json()["detail"][0]["msg"] == "field required"  # Assuming this is the validation message for empty name
def test_create_book_invalid_data():
    response = client.post(
        "/books",
        json={"title": "", "author_id": 1},
        auth    =("admin", "password123")   
    )   
    assert response.status_code == 422  # Unprocessable Entity for validation errors
    assert "title" in response.json()["detail"][0]["loc"]  # Check if the error is related to the 'title' field
    assert response.json()["detail"][0]["msg"] == "field required"  # Assuming this is the validation message for empty title
def test_search_authors_invalid_query():
    response = client.get("/search/authors", params={"name": ""}, auth=("admin", "password123"))
    assert response.status_code == 422  # Unprocessable Entity for validation errors
    assert "name" in response.json()["detail"][0]["loc"]  # Check if the error is related to the 'name' field
    assert response.json()["detail"][0]["msg"] == "field required"  # Assuming this is the validation message for empty name
def test_search_books_invalid_query():
    response = client.get("/search/books", params={"title": ""}, auth=("admin", "password123"))
    assert response.status_code == 422  # Unprocessable Entity for validation errors
    assert "title" in response.json()["detail"][0]["loc"]  # Check if the error is related to the 'title' field
    assert response.json()["detail"][0]["msg"] == "field required"  # Assuming this is the validation message for empty title
def test_get_books_by_author_invalid_id():
    response = client.get("/books/by_author/9999", params={"skip": 0, "limit": 10}, auth=("admin", "password123"))
    assert response.status_code == 404  # Not Found for non-existent author ID
    assert response.json() == {"detail": "Author not found"}  # Assuming this is the message for non-existent author
def test_get_books_by_author_name_invalid_name():
    response = client.get("/books/by_author_name/Non Existent Author", params={"limit": 10}, auth=("admin", "password123"))
    assert response.status_code == 404  # Not Found for non-existent author name
    assert response.json() == {"detail": "Author not found"}  # Assuming this is the message for non-existent author
def test_paginated_authors_invalid_params():
    response = client.get("/authors/paginated", params={"skip": -1, "limit": 10}, auth=("admin", "password123"))
    assert response.status_code == 422  # Unprocessable Entity for invalid pagination parameters
    assert response.json()["detail"][0]["msg"] == "value is not a valid integer"  # Assuming this is the validation message for negative skip value
    assert "skip" in response.json()["detail"][0]["loc"]  # Check if the error is related to the 'skip' field
def test_paginated_books_invalid_params():
    response = client.get("/books/paginated", params={"skip": -1, "limit": 10}, auth=("admin", "password123"))
    assert response.status_code == 422  # Unprocessable Entity for invalid pagination parameters
    assert response.json()["detail"][0]["msg"] == "value is not a valid integer"  # Assuming this is the validation message for negative skip value
    assert "skip" in response.json()["detail"][0]["loc"]  # Check if the error is related to the 'skip' field
def test_create_author_duplicate():
    # First create an author
    client.post(
        "/authors",
        json={"name": "Duplicate Author", "bio": "This author will be duplicated"},
        auth=("admin", "password123")
    )
    
    # Try to create the same author again
    response = client.post(
        "/authors",
        json={"name": "Duplicate Author", "bio": "This should fail due to duplication"},
        auth=("admin", "password123")
    )
    
    assert response.status_code == 400  # Bad Request for duplicate author
    assert response.json() == {"detail": "Author already exists"}  # Assuming this is the message for duplicate authors
def test_create_book_non_existent_author():
    response = client.post(
        "/books",
        json={"title": "Book with Non-existent Author", "author_id": 9999},
        auth=("admin", "password123")
    )
    assert response.status_code == 404  # Not Found for non-existent author ID
    assert response.json() == {"detail": "Author not found"}  # Assuming this is the message for non-existent author
def test_create_book_without_author_id():
    response = client.post(
        "/books",
        json={"title": "Book without Author ID"},
        auth=("admin", "password123")
    )
    assert response.status_code == 422  # Unprocessable Entity for missing author_id
    assert "author_id" in response.json()["detail"][0]["loc"]  # Check if the error is related to the 'author_id' field
    assert response.json()["detail"][0]["msg"] == "field required"  # Assuming this is the validation message for missing author_id
def test_create_author_without_name():
    response = client.post(
        "/authors",
        json={"bio": "This should fail due to missing name"},
        auth=("admin", "password123")
    )
    assert response.status_code == 422  # Unprocessable Entity for missing name 
    assert "name" in response.json()["detail"][0]["loc"]  # Check if the error is related to the 'name' field
    assert response.json()["detail"][0]["msg"] == "field required"  # Assuming this is the validation message for missing name
def test_create_book_without_title():
    response = client.post(
        "/books",
        json={"author_id": 1},auth=("admin", "password123")
    )   
    assert response.status_code == 422  # Unprocessable Entity for missing title    
    assert "title" in response.json()["detail"][0]["loc"]  # Check if the error is related to the 'title' field
    assert response.json()["detail"][0]["msg"] == "field required"  # Assuming this is the validation message for missing title 
def test_create_author_with_special_characters():
    response = client.post(
        "/authors",
        json={"name": "Author with Special Characters !@#$%^&*()", "bio": "Testing special characters"},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API allows special characters in names
    assert response.json()["usuario"]["name"] == "Author with Special Characters !@#$%^&*()"
def test_create_book_with_special_characters():
    response = client.post(
        "/books",
        json={"title": "Book with Special Characters !@#$%^&*()", "author_id": 1},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API allows special characters in titles
    assert response.json()["title"] == "Book with Special Characters !@#$%^&*()"        
def test_create_author_with_long_name():
    long_name = "A" * 256  # Assuming the name field has a maximum length of 255 characters
    response = client.post(
        "/authors",
        json={"name": long_name, "bio": "Testing long name"},
        auth=("admin", "password123")
    )
    assert response.status_code == 422  # Unprocessable Entity for exceeding maximum length
    assert "name" in response.json()["detail"][0]["loc"]  # Check if the error is related to the 'name' field
    assert response.json()["detail"][0]["msg"] == "string_too_long"  # Assuming this is the validation message for exceeding maximum length
def test_create_book_with_long_title():
    long_title = "B" * 256  # Assuming the title field has a maximum length of 255 characters
    response = client.post(
        "/books",
        json={"title": long_title, "author_id": 1},
        auth=("admin", "password123")
    )
    assert response.status_code == 422  # Unprocessable Entity for exceeding maximum length
    assert "title" in response.json()["detail"][0]["loc"]  # Check if the error is related to the 'title' field
    assert response.json()["detail"][0]["msg"] == "string_too_long"  # Assuming this is the validation message for exceeding maximum length
def test_create_author_with_empty_bio():
    response = client.post(
        "/authors",
        json={"name": "Author with Empty Bio", "bio": ""},
        auth    =("admin", "password123")
    )     
    assert response.status_code == 200  # Assuming the API allows empty bios
    assert response.json()["usuario"]["bio"] == ""  # Check if the bio is stored as empty string
def test_create_book_with_empty_summary():
    response = client.post(
        "/books",
        json={"title": "Book with Empty Summary", "author_id": 1, "summary": ""},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API allows empty summaries
    assert response.json()["summary"] == ""  # Check if the summary is stored as empty string
def test_create_author_with_unicode_name():
    response = client.post(
        "/authors",
        json={"name": "Author with Unicode ñ", "bio": "Testing unicode characters"},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API allows unicode characters in names
    assert response.json()["usuario"]["name"] == "Author with Unicode ñ"    
def test_create_book_with_unicode_title():
    response = client.post(
        "/books",
        json={"title": "Book with Unicode ñ", "author_id": 1},
        auth=("admin", "password123")
    )   
    assert response.status_code == 200  # Assuming the API allows unicode characters in titles
    assert response.json()["title"] == "Book with Unicode ñ"  # Check if the title is stored correctly
def test_create_author_with_leading_trailing_spaces():
    response = client.post(
        "/authors",
        json={"name": "  Author with Spaces  ", "bio": "Testing leading and trailing spaces"},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API allows leading and trailing spaces in names
    assert response.json()["usuario"]["name"] == "  Author with Spaces  "  # Check if the name is stored with spaces
def test_create_book_with_leading_trailing_spaces():
    response = client.post(
        "/books",
        json={"title": "  Book with Spaces  ", "author_id": 1},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API allows leading and trailing spaces in titles
    assert response.json()["title"] == "  Book with Spaces  "  # Check if the title is stored with spaces
def test_create_author_with_non_ascii_characters():
    response = client.post(
        "/authors",
        json={"name": "Autor con caracteres no ASCII ñ", "bio": "Testing non-ASCII characters"},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API allows non-ASCII characters in names
    assert response.json()["usuario"]["name"] == "Autor con caracteres no ASCII ñ"  # Check if the name is stored correctly 
def test_create_book_with_non_ascii_characters():
    response = client.post(
        "/books",
        json={"title": "Libro con caracteres no ASCII ñ", "author_id": 1},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API allows non-ASCII characters in titles
    assert response.json()["title"] == "Libro con caracteres no ASCII ñ"  # Check if the title is stored correctly  
def test_create_author_with_special_characters_in_bio():
    response = client.post(
        "/authors",
        json={"name": "Author with Special Characters in Bio", "bio": "Bio with !@#$%^&*()"},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API allows special characters in bios
    assert response.json()["usuario"]["bio"] == "Bio with !@#$%^&*()"  # Check if the bio is stored correctly       
def test_create_book_with_special_characters_in_summary():
    response = client.post(
        "/books",
        json={"title": "Book with Special Characters in Summary", "author_id": 1, "summary": "Summary with !@#$%^&*()"},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API allows special characters in summaries
    assert response.json()["summary"] == "Summary with !@#$%^&*()"  # Check if the summary is stored correctly  
def test_create_author_with_html_tags():
    response = client.post(
        "/authors",
        json={"name": "Author with <b>HTML</b> Tags", "bio": "Bio with <i>italic</i> text"},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API allows HTML tags in names and bios
    assert response.json()["usuario"]["name"] == "Author with <b>HTML</b> Tags"  # Check if the name is stored correctly
    assert response.json()["usuario"]["bio"] == "Bio with <i>italic</i> text"  # Check if the bio is stored correctly       
def test_create_book_with_html_tags():

    response = client.post(
        "/books",
        json={"title": "Book with <b>HTML</b> Tags", "author_id": 1, "summary": "Summary with <i>italic</i> text"},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API allows HTML tags in titles and summaries
    assert response.json()["title"] == "Book with <b>HTML</b> Tags"  # Check if the title is stored correctly
    assert response.json()["summary"] == "Summary with <i>italic</i> text"  # Check if the summary is stored correctly      
def test_create_author_with_sql_injection():
    response = client.post(
        "/authors",
        json={"name": "Author with SQL Injection ' OR '1'='1", "bio": "Testing SQL injection"},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API handles SQL injection safely
    assert response.json()["usuario"]["name"] == "Author with SQL Injection ' OR '1'='1"  # Check if the name is stored correctly
def test_create_book_with_sql_injection():  
    response = client.post(
        "/books",
        json={"title": "Book with SQL Injection ' OR '1'='1", "author_id": 1},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API handles SQL injection safely
    assert response.json()["title"] == "Book with SQL Injection ' OR '1'='1"  # Check if the title is stored correctly      
def test_create_author_with_xss_attack():
    response = client.post(
        "/authors",
        json={"name": "Author with XSS <script>alert('XSS')</script>", "bio": "Testing XSS attack"},
        auth=("admin", "password123")
    )
    assert response.status_code == 200  # Assuming the API handles XSS attacks safely
    assert response.json()["usuario"]["name"] == "Author with XSS <script>alert('XSS')</script>"  # Check if the name is stored correctly   
def test_create_book_with_xss_attack():
    response = client.post(
        "/books",
        json={"title": "Book with XSS <script>alert('XSS')</script>", "author_id": 1},
        auth    =("admin", "password123")       
    )
    assert response.status_code == 200  # Assuming the API handles XSS attacks safely   
    assert response.json()["title"] == "Book with XSS <script>alert('XSS')</script>"  # Check if the title is stored correctly

"""