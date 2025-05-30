from sqlalchemy.orm import Session
from database import SessionLocal
from models import AuthorDB as Author, BookDB as Book

def seed():
    db: Session = SessionLocal()

    # Limpiar tablas primero (opcional, solo para tests)
    db.query(Book).delete()
    db.query(Author).delete()

    # Crear autores
    author1 = Author(id=1,name="Gabriel García Márquez",bio=None)
    author2 = Author(id=2,name="Isabel Allende", bio=None)

    db.add_all([author1, author2])
    db.commit()

    # Crear libros asociados
    book1 = Book(id=10,title="Cien años de soledad", summary = None, published_date="01/01/1967", author_id=author1.id)
    book2 = Book(id=20,title="El amor en los tiempos del cólera", summary = None, published_date="01/01/1985", author_id=author1.id)
    book3 = Book(id=30,title="La casa de los espíritus", summary = None, published_date="01/01/1982", author_id=author2.id)

    db.add_all([book1, book2, book3])
    db.commit()

    db.close()
    print("✅ Datos de prueba insertados correctamente.")

if __name__ == "__main__":
    seed()
