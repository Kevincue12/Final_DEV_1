from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://utlvcrk2oo2wusguzte5:RnRWR6HcJlVBYlUZDCOy7s9gU2GTeU@brrqzjmolba4h2vq0nct-postgresql.services.clever-cloud.com:5432/brrqzjmolba4h2vq0nct"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()