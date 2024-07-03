from typing import List
from pydantic import BaseModel
from app.schemas.parts import Angle, Coord

class ExerciseName(BaseModel):
    id: int
    name: str = ""

class NewExercise(BaseModel):
    name: str = ""
    data: str = ""
    video: str = ""

class Exercise(NewExercise):
    id: int

    class Config:
        from_attributes = True
