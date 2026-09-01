import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
#loading variables from .env
load_dotenv()

#access variable
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine("DATABASE_URL")

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

#declarative base class for sqlalchemy
class Base(DeclarativeBase):
    pass


#dependency injection
def get_db():
    db = SessionLocal() #instantiate object
    try:
        yield db
    finally:
        db.close() #close connection after request
