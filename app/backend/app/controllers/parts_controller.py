from sqlalchemy.orm import Session
from app import models, schemas

def initialise_parts(db: Session, angles_names: list[str], coord_names: list[str]):
    """
    Inicializa las partes que pueden usarse en un ejercicio
    """
    angles = []
    if count_angles(db) == 0:
        for i in angles_names:
            angles.append(models.Angle(angle = i))
        db.bulk_save_objects(angles)
    coords = []
    if count_coords(db) == 0:
        for i in coord_names:
            coords.append(models.Coord(coord = i))
        db.bulk_save_objects(coords)
    db.commit()

def create_amgles(db: Session, exercise_id: int, angles_names: list[schemas.Angle]):
    """
    Asigna los angulos a un ejercicio con el id que se le pasa por parametro.
    """
    angles = []
    for i in angles_names:
        angles.append(models.ExerciseAngle(exercise_id = exercise_id, angle_id= i.angle))
    db.bulk_save_objects(angles)
    db.commit()

def create_coords(db: Session, exercise_id: int, coord_names: list[schemas.Coord]):
    """
    Asigna las coordenadas a un ejercicio con el id que se le pasa por parametro.
    """
    coords = []
    for i in coord_names:
        coords.append(models.ExerciseCoord(exercise_id = exercise_id, coord_id= i.coord))
    db.bulk_save_objects(coords)
    db.commit()

def get_angles_from_exercise(db: Session, exercise_id: int):
    """
    Obtener los angulos de un ejercicio.
    """
    return db.query(models.ExerciseAngle).filter(models.ExerciseAngle.exercise_id == exercise_id).all()

def get_coords_from_exercise(db: Session, exercise_id: int):
    """
    Obtiene las coordenadas de un ejercicio.
    """
    return db.query(models.ExerciseCoord).filter(models.ExerciseCoord.exercise_id == exercise_id).all()

def count_angles(db: Session):
    """
    Cuenta los angulos.
    """
    return db.query(models.Angle).count()

def get_all_angles(db: Session):
    """
    Obtener los angulos.
    """
    return db.query(models.Angle).all()

def count_coords(db: Session):
    """
    Cuenta las coordenadas.
    """
    return db.query(models.Coord).count()

def get_all_coords(db: Session):
    """
    Devuelve todas las coordenadas.
    """
    return db.query(models.Coord).all()

def remove_angles_from_exercise(db: Session,  exercise_id: int):
    """
    Borra los angulos de un ejercicio.
    """
    db.query(models.ExerciseAngle).filter(models.ExerciseAngle.exercise_id == exercise_id).delete()
    db.commit()
    return True

def remove_coords_from_exercise(db: Session, exercise_id: int):
    """
    Borra las coordenadas de un ejercicio.
    """
    db.query(models.ExerciseCoord).filter(models.ExerciseCoord.exercise_id == exercise_id).delete()
    db.commit()
    return True