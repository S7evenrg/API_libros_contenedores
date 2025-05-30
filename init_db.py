from sqlalchemy import inspect
from database import Base, engine
from models import AuthorDB as Author, BookDB as Book

def init():
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas exitosamente.")

def check_and_create_tables():
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()

    print("🔍 Verificando tablas en la base de datos...")

    all_models = [Author.__tablename__, Book.__tablename__]
    #all_models = [Author, Book]
    
    for table in all_models:
        if table in existing_tables:
            print(f"✅ Tabla '{table}' ya existe.")
        else:
            print(f"⚠️ Tabla '{table}' no existe. Será creada.")
            #table.create(bind=engine, checkfirst=True)

    Base.metadata.create_all(bind=engine)
    print("✅ Proceso completado.")