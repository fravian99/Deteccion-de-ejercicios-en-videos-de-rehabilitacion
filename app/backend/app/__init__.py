import os
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from app.database import engine
from app import models, schemas
from app.routes import exercise, user
from app.config import settings
import app.config
import app.auth as auth
from app.controllers import user_controller, auth_controller
from sqlalchemy.orm import Session

ADMIN = "admin"

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost",
    "http://localhost:4200",
    "127.0.0.1"
]

app = FastAPI()
app.add_middleware(CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"],
)

def init_db():
    with Session(engine) as session:
        user = user_controller.get_user_by_username(session, settings.FIRST_SUPERUSER)
        if not user:
            auth_base = schemas.AuthBase(username=settings.FIRST_SUPERUSER, password=settings.FIRST_SUPERUSER_PASSWORD)
            user = auth_controller.create_user(session, auth_base)
            user.rol = ADMIN
            session.commit()

@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.get("/test")
async def test():
    return {"message": "Hello World"}


init_db()
app.include_router(exercise.router)
app.include_router(user.router)
