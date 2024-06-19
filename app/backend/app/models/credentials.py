"""
Tablas de credenciales
"""
from sqlalchemy import Column, ForeignKey, String
from app.database import Base
from app.models.user import User

class Credentials(Base):
    """
    Tabla que contiene las contraseñas
    """
    __tablename__ = "Credentials"
    id = Column(String, ForeignKey(User.id), primary_key=True)
    password = Column(String, nullable=False)

    def __init__(self, user_id: str, password: str):
        self.id = user_id
        self.password = password

