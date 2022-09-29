from typing import Optional, List
import fastapi
from api.utils.users import get_user,get_user_by_email, get_users
router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@router.get("/users/{id}")
async def get_user(id: int):
    return { "user": users[id] }
