from typing import Optional, List
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]
    age: int


@router.get("/", response_model=List[User])
async def get_user():
    return users


@router.post("/user")
async def create_user(user: User):
    users.append(user)
    return users


@router.get("/users/{id}")
async def get_user(id: int):
    return {"users": users[id]}