from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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

#NOTA: no usar db = get_db(), se debe usar siempre el yield