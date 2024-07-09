from sqlalchemy.orm import Session
from app import schemas, utils, models

def get_user_by_id(db: Session, user_id: str):
    """
    Devuelve el usuario con id determinado
    """
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    """
    Devuelve el usuario segun el nombre que se pasa por parametro.
    """
    return db.query(models.User).filter(models.User.username == username).first()