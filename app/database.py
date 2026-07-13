from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from app.env import database_url
DATABASE_URL = database_url
engine = create_engine(DATABASE_URL)

session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db
