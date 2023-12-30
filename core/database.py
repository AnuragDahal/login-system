from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

# load_dotenv()  # take environment variables from .env.

SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

# Check if DATABASE_URL is None
if SQLALCHEMY_DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set in the environment variables.")
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
