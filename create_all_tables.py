from database import Base, engine
from models import AuthorDB as Author, BookDB as Book

def init():
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas exitosamente.")

if __name__ == "__main__":
    init()
