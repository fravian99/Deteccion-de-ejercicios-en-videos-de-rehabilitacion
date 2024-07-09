from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.exercise import Exercise
from app.models.parts import Coord, Angle


class ExerciseCoord(Base):
    __tablename__ = "EXERCISE_COORD"
    exercise_id= Column(Integer,ForeignKey(Exercise.id), primary_key=True)
    coord_id= Column(String,ForeignKey(Coord.coord), primary_key=True)
    coord = relationship('Coord', back_populates='exercises')
    exercise = relationship('Exercise', back_populates='coords')

class ExerciseAngle(Base):
    __tablename__ = "EXERCISE_ANGLE"
    exercise_id= Column(Integer,ForeignKey(Exercise.id), primary_key=True)
    angle_id= Column(String,ForeignKey(Angle.angle), primary_key=True)
    angle = relationship('Angle',back_populates='exercises')
    exercise = relationship('Exercise',back_populates='angles')