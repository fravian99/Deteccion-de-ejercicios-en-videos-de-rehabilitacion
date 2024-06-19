import os
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from app.database import engine
from app import models
from app.routes import exercise, user
from app.config import settings
import app.config
import app.auth as auth

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

@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.get("/test")
async def main():
    return {"message": "Hello World"}

@app.get("/video/{ej}")
async def get_video(ej, get_current_user: int = Depends(auth.get_current_user)):
    
    def iterfile(video_path):
        with open(video_path, mode="rb") as file_like:
            yield from file_like
    path = "app" + os.sep +"data"+ os.sep + "videos"
    if (ej == "pelota2"):
        video_path = path + os.sep + "josemi_pelota2_1.mp4"

        return StreamingResponse(iterfile(video_path), media_type="video/mp4")
        #return FileResponse(video_path)
    return 

app.include_router(exercise.router)
app.include_router(user.router)