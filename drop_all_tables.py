from database import Base, engine
from models import Author, Book  # Importa los modelos para que estén registrados

def drop_all():
    print("🧨 Eliminando todas las tablas...")
    Base.metadata.drop_all(bind=engine)
    print("✅ Tablas eliminadas correctamente.")

if __name__ == "__main__":
    drop_all()
