from sqlalchemy.orm import Session
from db.models.user import User
from pydantic_schemas.user import UserCreate

def get_user(db:)