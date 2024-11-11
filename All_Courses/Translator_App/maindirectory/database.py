import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

def get_db():
    db=SessionLocal() #oturum aç
    try:
        yield db 
    finally:
        db.close() #işlem bitince dbyi kapat

SQLALCHEMY_DATABASE_URL=os.getenv("DATABASE_URL")
engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)