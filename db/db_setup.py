from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres@localhost/fastapi_student"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/fastapi_student"
 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)
SessionLocal = sessionmaker(autocommit=False, future=True, autoflush=False, bind=engine)
 
Base = declarative_base()

#DB Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()