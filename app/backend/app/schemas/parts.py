from pydantic import BaseModel

class Angle(BaseModel):
    angle: str

class Coord(BaseModel):
    coord: str