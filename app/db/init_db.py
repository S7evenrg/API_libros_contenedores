from sqlalchemy import inspect
from app.db.database import Base, engine, wait_for_mysql
from app.db.models import AuthorDB as Author, BookDB as Book


def init():
    wait_for_mysql()  
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)


def check_and_create_tables():
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()

    print("Verificando tablas en la base de datos...")

    all_models = [Author.__tablename__, Book.__tablename__]
    
    for table in all_models:
        if table in existing_tables:
            print(f"✅ Tabla '{table}' ya existe.")
        else:
            print(f"⚠️ Tabla '{table}' no existe. Será creada.")

    Base.metadata.create_all(bind=engine)
    print("✅ Proceso completado.")
