"""
Tablas de ejercicios
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Exercise(Base):
    """
    Tabla que contiene los ejercicios
    """
    __tablename__ = "EXERCISE"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    data = Column(String)
    video = Column(String)
    angles = relationship("ExerciseAngle", back_populates="exercise")
    coords = relationship("ExerciseCoord", back_populates="exercise")
