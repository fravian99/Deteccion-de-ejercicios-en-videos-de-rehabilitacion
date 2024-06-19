from sqlalchemy import Column, String
from app.database import Base
import uuid

class User(Base):
    __tablename__ = "User"
    id = Column(String, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    rol = Column(String, default="paciente")

    def __init__(self, username: str):
        self.id = str(uuid.uuid4())
        self.rol = "paciente"
        self.username = username
