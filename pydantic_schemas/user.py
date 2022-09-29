from ast import List
from datetime import datetime
from sys import intern
from pydantic import BaseModel
import enum
from datetime import datetime

class UserBase(BaseModel):
    email: str
    role : intern


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at:datetime

    class Config:
        orm_mode = True
