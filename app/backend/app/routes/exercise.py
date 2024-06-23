

from typing import Annotated

from fastapi import Depends, File, Form, HTTPException, UploadFile, status, APIRouter
from fastapi.responses import FileResponse
import os
from app.database import get_db
from app.utils import save_file, delete_file
from app import auth, schemas 
from app.controllers import exercise_controller

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
        exercise = schemas.BaseExercise()
        exercise.name = name
        exercise.data = datapath
        exercise.video = videopath
        exercise_controller.create_exercise(db, exercise)
        
    except Exception as ex:
        raise ex
    return True

@router.delete("/delete-exercise/{id}")
async def delete_exercise(id: int, db: Session = Depends(get_db)):
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