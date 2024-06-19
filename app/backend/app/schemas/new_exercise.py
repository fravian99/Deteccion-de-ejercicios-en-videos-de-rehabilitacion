from pydantic import BaseModel

from fastapi import Form, UploadFile

class NewExercise(BaseModel):
    name: str = Form(...)
    video: UploadFile = Form(...)