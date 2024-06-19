from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Exercise(Base):
    __tablename__ = "Exercise"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    video = Column(String)