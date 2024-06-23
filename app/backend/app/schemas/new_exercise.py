from pydantic import BaseModel

from fastapi import Form, UploadFile

class BaseExercise(BaseModel):
    name: str = ""
    data: str = ""
    video: str = ""

class Exercise(BaseExercise):
    id: int

    class Config:
        from_attributes = True
