<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Data_Base_SQL import crud, schemas, database
from typing import List

# Definiere den Router für Workouts
router = APIRouter(
    prefix="/workouts",
    tags=["Workouts"]
)


# Datenbank-Abhängigkeit (Dependency)
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------- POST (Neues Workout Erstellen) --------------------
# Laut ERD muss ein Workout einem Benutzer zugeordnet werden (user_id ist FK)
@router.post("/", response_model=schemas.WorkoutRead, status_code=status.HTTP_201_CREATED)
def create_workout_for_user(workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    # AUFGABE: Prüfen, ob der Benutzer existiert, bevor das Workout erstellt wird (Fehler 404 verhindern)
    db_user = crud.get_user_by_id(db, user_id=workout.user_id)
    if db_user is None:
        # Fehler ausgeben, wenn der Fremdschlüssel (User ID) ungültig ist
        raise HTTPException(status_code=404, detail=f"Benutzer mit ID {workout.user_id} wurde nicht gefunden.")

    # CRUD-Funktion aufrufen, um das Workout zu speichern
    return crud.create_workout(db=db, workout=workout)


# -------------------- GET (Alle Workouts Lesen) --------------------
@router.get("/", response_model=List[schemas.WorkoutRead])
def read_workouts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # RUFEN: Alle Workouts aus der Datenbank abrufen
    workouts = crud.get_workouts(db, skip=skip, limit=limit)
    return workouts


# -------------------- GET (Einzelnes Workout Lesen) --------------------
@router.get("/{workout_id}", response_model=schemas.WorkoutRead)
def read_workout(workout_id: int, db: Session = Depends(get_db)):
    # RUFEN: Ein spezifisches Workout anhand der ID abrufen
    db_workout = crud.get_workout_by_id(db, workout_id=workout_id)
    if db_workout is None:
        raise HTTPException(status_code=404, detail="Workout nicht gefunden")
    return db_workout
=======
from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.orm import Session

from Class_Functions.Workout_Generator import WorkoutGenerator
from Data_Base_SQL.crud import create_workout
from Data_Base_SQL.database import get_db
from Data_Base_SQL.schemas import WorkoutCreate, WorkoutRead

app = APIRouter(prefix="/workout", tags=["Workout"])


# -----------------------------------
# GENERATE WORKOUT PLAN (no database)
# -----------------------------------
@app.get("/{days}")
def generate_workout(days: int):
    generator = WorkoutGenerator()
    return generator.generate_plan(days)


# -----------------------------------
# CREATE WORKOUT (UUID-compatible)
# -----------------------------------
@app.post("/workouts", response_model=WorkoutRead)
def create_workout_endpoint(payload: WorkoutCreate, db: Session = Depends(get_db)):
    workout = create_workout(db, payload)

    if not workout:
        raise HTTPException(status_code=400, detail="Workout konnte nicht erstellt werden")

    return workout
>>>>>>> 0be12a57868a06cd9b7e823ed7fd36984d314e81
