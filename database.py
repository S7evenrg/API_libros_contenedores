from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
import time

#DATABASE_URL = "sqlite:///./database/biblioteca.db"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_HOSTNAME = "libros_db"
MYSQL_PORT = 3306
MYSQL_DB = "biblioteca"

DATABASE_URL_NO_DB = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:{MYSQL_PORT}/"
DATABASE_URL = f"{DATABASE_URL_NO_DB}{MYSQL_DB}"

#DATABASE_URL = "sqlite:///./database/biblioteca.db"


#engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def wait_for_mysql():
    print("⏳ Esperando que MySQL esté disponible...")
    for i in range(10):
        try:
            conn = pymysql.connect(
                host="libros_db",  # Usa el nombre del servicio en docker-compose
                user="root",
                password="root",
                database="biblioteca",
                port=3306
            )
            conn.close()
            print("✅ MySQL está listo.")
            return
        except pymysql.MySQLError as e:
            print(f"Intento {i+1}/10 fallido: {e}")
            time.sleep(2)
    raise Exception("❌ No se pudo conectar a MySQL después de 10 intentos.")


#NOTA: no usar db = get_db(), se debe usar siempre el yield