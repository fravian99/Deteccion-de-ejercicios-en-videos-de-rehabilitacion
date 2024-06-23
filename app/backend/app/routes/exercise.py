
import os
from typing import Annotated

from fastapi import Depends, File, Form, HTTPException, UploadFile, status, APIRouter
from fastapi.responses import FileResponse, StreamingResponse
from app.database import get_db
from app.utils import save_file, delete_file, open_video
from app import auth, schemas
from app.controllers import exercise_controller
from app.models import Exercise

from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/exercise',
    tags=['Exercise']
)
APPROUTE = "./app/data"

@router.post("/new-exercise")
async def new_exercise(name: Annotated[str, Form()], data: Annotated[UploadFile, File()] ,
                       video: Annotated[UploadFile, File()],
                       get_current_user: int = Depends(auth.get_current_user),
                       db: Session = Depends(get_db)):
    try:
        datapath = save_file(data, "pos", APPROUTE)
        videopath = save_file(video, "mp4", APPROUTE)
        exercise = schemas.NewExercise(name = name, data = datapath, video = videopath)
        exercise_controller.create_exercise(db, exercise)
        
    except Exception as ex:
        raise ex
    return True

@router.delete("/delete-exercise/{id}")
async def delete_exercise(id: int, get_current_user: int = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    exercise = exercise_controller.get_exercise(db, id)
    if (exercise is None):
        raise HTTPException(
            status_code=404,
            detail="Exercise not found",
            headers={"X-Error": "Exercise Not Found"},
        )
    exercise_controller.remove_excercise(db, exercise)
    delete_file(exercise.data, APPROUTE)
    delete_file(exercise.video, APPROUTE)
    return True

@router.get("/get-exercises")
async def get_exercises(get_current_user: int = Depends(auth.get_current_user), db:Session = Depends(get_db)):
    exercises: list [Exercise] = exercise_controller.get_all_exercises(db)
    exercises_names = [schemas.ExerciseName(id = exercise.id, name = exercise.name) for exercise in exercises]
    return {"exercises": exercises_names}

@router.get("/get-video/{id}")
async def get_video(id, get_current_user: int = Depends(auth.get_current_user), db:Session = Depends(get_db)):
    exercise = exercise_controller.get_exercise(db, id)   
    path = exercise.video
    video = open_video(path, APPROUTE)        
    return video

@router.get("/get-exercise/{id}")
async def get_exercise(id, get_current_user: int = Depends(auth.get_current_user), db:Session = Depends(get_db)):
    exercise = exercise_controller.get_exercise(db, id)   
    exercise_schema = schemas.ExerciseName(id = exercise.id, name = exercise.name)
    return exercise_schema

@router.post("/send-user-exercise/{id}")
async def post_user_exercise(id: int, 
                             data: Annotated[UploadFile, File()], 
                             get_current_user: int = Depends(auth.get_current_user), 
                             db:Session = Depends(get_db)):
    exercise = exercise_controller.get_exercise(db, id)
    profesional_path = os.path.join(APPROUTE, exercise.data)
    with open(profesional_path, "rb") as profesional:  
        comparation = 10
    return comparation

