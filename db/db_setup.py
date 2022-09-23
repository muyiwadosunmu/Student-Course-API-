from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://muyiwa@loclhost/fast_api"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

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