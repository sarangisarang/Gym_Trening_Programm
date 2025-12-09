from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Data_Base_SQL import schemas
from Data_Base_SQL import crud
from Data_Base_SQL.database import get_db

router = APIRouter(
    prefix="/workout_exercises",
    tags=["Workout Exercises"]
)

@router.post("/")
def create_workout_exercise_link(
        item: schemas.WorkoutExerciseCreate,
        db: Session = Depends(get_db)
):
    db_link = crud.create_workout_exercise(db=db, item=item)

    return db_link