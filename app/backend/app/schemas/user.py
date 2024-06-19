from pydantic import BaseModel

from fastapi import Form, UploadFile

class UserBase(BaseModel):
    username: str
    password: str 