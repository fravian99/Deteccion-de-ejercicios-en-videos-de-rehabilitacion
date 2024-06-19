from pydantic import BaseModel


class AuthBase(BaseModel):
    username: str
    password: str
