from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.database import Base


class Coord(Base):
    """
    Tabla que guarda los nombres de las coordenadas.
    """
    __tablename__ = "COORD"
    coord = Column(String, primary_key=True)
    exercises = relationship("ExerciseCoord", back_populates="coord")

class Angle(Base):
    """
    Tabla que guarda los angulos.
    """
    __tablename__ = "ANGLE"
    angle = Column(String, primary_key=True)
    exercises = relationship('ExerciseAngle',back_populates='angle')
