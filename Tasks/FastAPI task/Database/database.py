from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DB_PASSWORD,DB_USERNAME


SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost/FreeResources'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
