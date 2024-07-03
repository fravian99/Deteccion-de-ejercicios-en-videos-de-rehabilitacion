from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.database import Base


class Coord(Base):
    __tablename__ = "COORD"
    coord = Column(String, primary_key=True)
    exercises = relationship("ExerciseCoord", back_populates="coord")

class Angle(Base):
    __tablename__ = "ANGLE"
    angle = Column(String, primary_key=True)
    exercises = relationship('ExerciseAngle',back_populates='angle')
