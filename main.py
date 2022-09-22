from fastapi import FastAPI, Path, Query
from typing import Optional, List

from api import users, courses, sections

app = FastAPI(
    title="Fast API CRUD Project",
    description="API for managing students and courses",
    contact = {
        "name": "Oluwamuyiwa",
        "email": "oluwadosunmu@gmail.com"
    }
)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)


