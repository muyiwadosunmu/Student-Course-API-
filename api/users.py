from typing import Optional, List
import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from api.utils.users import create_user, get_user,get_user_by_email, get_users
from db.db_setup import get_db
from api.utils.courses import get_user_courses
from pydantic_schemas.user import UserCreate, UserBase, User
from pydantic_schemas.course import Course 


router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    users = get_users(db=db, skip=skip, limit=limit )
    return users


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db:Session=Depends(get_db)):
    db_user = get_user_by_email(db=db,email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    return create_user(db=db, user=user)


@router.get("/users/{id}", response_model=User)
async def read_user(user_id: int,db:Session=Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, details ="User not found")
    return db_user


@router.get("/users/{user_id}/courses", response_model= List[Course])
async def read_user_courses(user_id:int, db:Session=Depends(get_db)):
    courses = get_user_courses(db=db, user_id=user_id)
    return courses