from fastapi import FastAPI
from api import users, courses, sections
from db.db_setup import engine, SessionLocal, get_db
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast API CRUD Project",
    description="API for managing students and courses",
    contact={"name": "Oluwamuyiwa", "email": "oluwadosunmu@gmail.com"},
)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
