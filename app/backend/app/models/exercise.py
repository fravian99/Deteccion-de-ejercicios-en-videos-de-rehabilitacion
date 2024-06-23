"""
Tablas de ejercicios
"""
from sqlalchemy import Column, Integer, String

from app.database import Base

class Exercise(Base):
    """
    Tabla que contiene los ejercicios
    """
    __tablename__ = "Exercise"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    data = Column(String)
    video = Column(String)
