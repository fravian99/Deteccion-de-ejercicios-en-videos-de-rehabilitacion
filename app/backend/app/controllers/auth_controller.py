from sqlalchemy.orm import Session
from app import schemas, utils, models

def create_user(db: Session, user: schemas.AuthBase):
    password = utils.hash_password(user.password)
    db_user = models.User(user.username)
    db.add(db_user)
    savepoint = db.begin_nested()

    db_auth = models.Credentials(db_user.id, password)
    db.add(db_auth)

    db.commit()
    db.refresh(db_user)
    return db_user

def get_credentials_by_id(db: Session, user_id):
    return db.query(models.Credentials).filter(models.Credentials.id == user_id).first()