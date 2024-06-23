from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import DatabaseError
from app.config import settings

SQLALCHEMY_DATABASE=""
if settings.PRODUCTION:
    SQLALCHEMY_DATABASE= f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
else:
    SQLALCHEMY_DATABASE = 'sqlite:///./app.db'

engine: Engine = create_engine(
    SQLALCHEMY_DATABASE
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except DatabaseError:
        db.close()
    finally:
        db.close()
