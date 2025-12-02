from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Data_Base_SQL.database import get_db
from Data_Base_SQL import crud, schemas ,models


router = APIRouter(prefix="/exercises", tags=["Exercises"])

@router.post("/")
def create_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(get_db)):
    return crud.create_exercise(db, exercise)

@router.get("/")
def list_exercises(db: Session = Depends(get_db)):
    return crud.get_exercises(db)


@router.post("/user/{user_id}")
def create_user_exercise(user_id: int, exercise: schemas.ExerciseCreate, db: Session = Depends(get_db)):
    return crud.create_exercise_for_user(db, user_id, exercise)


@router.get("/user/{user_id}")
def get_user_exercises(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Exercise).filter(models.Exercise.user_id == user_id).all()
