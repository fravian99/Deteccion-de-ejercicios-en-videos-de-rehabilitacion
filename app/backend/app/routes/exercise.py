
import os
from typing import Annotated
from fastapi import Depends, File, Form, HTTPException, UploadFile, APIRouter
from sqlalchemy.orm import Session

from app.database import get_db
from app.utils import save_file, delete_file, open_video
from app import auth, schemas
from app.controllers import exercise_controller, parts_controller
from app.models import Exercise
from app.dtw_calc.calc import compare

from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/exercise',
    tags=['Exercise']
)
APPROUTE = "./app/data"
VIDEO_DIR = os.path.join(APPROUTE,"video")
DATA_DIR = os.path.join(APPROUTE,"data")

@router.post("/new-exercise")
async def new_exercise(name: Annotated[str, Form()],
                       data: Annotated[UploadFile, File()] ,
                       video: Annotated[UploadFile, File()],
                       angles: Annotated[list, Form()],
                       coords: Annotated[list, Form()],
                       get_current_user: int = Depends(auth.get_editor_user),
                       db: Session = Depends(get_db)):
    try:
        
        datapath = save_file(data, "pos", DATA_DIR)
        videopath = save_file(video, "mp4", VIDEO_DIR)
        angles_schemas = [schemas.Angle(angle = angle) for angle in angles]
        coords_schemas = [schemas.Coord(coord = coord) for coord in coords]
        exercise = schemas.NewExercise(name = name, data = datapath, video = videopath, angles=angles_schemas, coords= coords_schemas)
        exercise_db = exercise_controller.create_exercise(db, exercise)
        parts_controller.create_amgles(db, exercise_db.id, angles_schemas)
        parts_controller.create_coords(db, exercise_db.id, coords_schemas)
    except Exception as ex:
        raise ex
    return True

@router.delete("/delete-exercise/{id}")
async def delete_exercise(id: int,
                          get_editor_user: int = Depends(auth.get_editor_user),
                          db: Session = Depends(get_db)):
    exercise = exercise_controller.get_exercise(db, id)
    if (exercise is None):
        raise HTTPException(
            status_code=404,
            detail="Exercise not found",
            headers={"X-Error": "Exercise Not Found"},
        )
    parts_controller.remove_angles_from_exercise(db, exercise.id)
    parts_controller.remove_coords_from_exercise(db, exercise.id)
    exercise_controller.remove_excercise(db, exercise)
    delete_file(exercise.data, DATA_DIR)
    delete_file(exercise.video, VIDEO_DIR)
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
    video = open_video(path, VIDEO_DIR)
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
    profesional_path = os.path.join(DATA_DIR, exercise.data)
    with open(profesional_path, "rb") as profesional:  
        comparation = compare(data.file, profesional)
    return comparation


@router.get("/default-parts")
async def get_default_parts(db: Session = Depends(get_db)):
    res = {}
    res["angles"] = parts_controller.get_all_angles(db)
    res["coords"] = parts_controller.get_all_coords(db)
    return res
