from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="Fast API CRUD Project",
    description="API for managing students and courses",
    contact = {
        "name": "Oluwamuyiwa",
        "email": "oluwadosunmu@gmail.com"
    }
)

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio:Optional[str]
    age: int


@app.get("/users", response_model=List[User])
async def get_user():
    return users


@app.post("/user")
async def create_user(user: User):
    users.append(user)
    return users

@app.get("/users/{id}")
async def get_user(
    id:int = Path(..., description="The ID of the user you want to retrieve"),
    is_active:str = Query(None,max_length=5)
):
    return {"users": users[id], "query":q}
