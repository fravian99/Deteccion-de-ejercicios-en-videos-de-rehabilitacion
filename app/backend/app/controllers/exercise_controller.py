from sqlalchemy.orm import Session
from app import models, schemas

def create_exercise(db: Session, exercise: schemas.NewExercise):
    db_exercise = models.Exercise(**exercise.model_dump())
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

def get_exercise(db: Session, exercise_id: int):
    return db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()

def get_all_exercises(db: Session):
    return db.query(models.Exercise).all()

def remove_excercise(db: Session, exercise: models.Exercise):
    db.delete(exercise)
    db.commit()
    return True
