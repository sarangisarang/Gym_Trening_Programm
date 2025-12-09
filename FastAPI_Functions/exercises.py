<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Data_Base_SQL import crud, schemas, database


# Definiert und exportiert das 'router'-Objekt, das in main.py benötigt wird
router = APIRouter(
    prefix="/exercises",
    tags=["Exercises"]
)


# Dependency, um die Datenbank-Session zu erhalten (Wiederverwendung der Funktion aus database.py)
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.ExerciseRead, status_code=status.HTTP_201_CREATED)
def create_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(get_db)):
    # Annahme: 'create_exercise' Funktion ist in crud.py definiert
    return crud.create_exercise(db=db, exercise=exercise)

@router.get("/", response_model=list[schemas.ExerciseRead])
def read_exercises(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Annahme: 'get_exercises' Funktion ist in crud.py definiert
    exercises = crud.get_exercises(db, skip=skip, limit=limit)
    return exercises

@router.get("/{exercise_id}", response_model=schemas.ExerciseRead)
def read_exercise(exercise_id: int, db: Session = Depends(get_db)):
    # Annahme: 'get_exercise' Funktion ist in crud.py definiert
    db_exercise = crud.get_exercise(db, exercise_id=exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return db_exercise
=======
from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.orm import Session
from Data_Base_SQL.database import get_db
from Data_Base_SQL import crud, schemas

app = APIRouter(prefix="/exercises", tags=["Übungen"])


# -----------------------------
# ÜBUNG ERSTELLEN (ohne Benutzer)
# -----------------------------
@app.post("/", response_model=schemas.ExerciseRead)
def create_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(get_db)):
    existing = crud.get_exercises(db)

    for ex in existing:
        if ex.title.lower() == exercise.title.lower() and ex.muscle_group.lower() == exercise.muscle_group.lower():
            raise HTTPException(status_code=400, detail="Diese Übung existiert bereits")

    return crud.create_exercise(db, exercise)


# -----------------------------
# ALLE ÜBUNGEN ANZEIGEN
# -----------------------------
@app.get("/", response_model=list[schemas.ExerciseRead])
def list_exercises(db: Session = Depends(get_db)):
    exercises = crud.get_exercises(db)

    if not exercises:
        raise HTTPException(status_code=404, detail="Keine Übungen gefunden")

    return exercises


# -----------------------------
# ÜBUNG FÜR EINEN BESTIMMTEN BENUTZER ERSTELLEN
# -----------------------------
@app.post("/user/{user_id}", response_model=schemas.ExerciseRead)
def create_user_exercise(
    user_id: UUID,
    exercise: schemas.ExerciseCreate,
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")

    return crud.create_exercise_for_user(db, user_id, exercise)


# -----------------------------
# ÜBUNGEN EINES BESTIMMTEN BENUTZERS ANZEIGEN
# -----------------------------
@app.get("/user/{user_id}", response_model=list[schemas.ExerciseRead])
def get_user_exercises(user_id: UUID, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")

    return crud.get_exercises_by_user(db, user_id)


# -----------------------------
# ÜBUNG LÖSCHEN
# -----------------------------
@app.delete("/{exercise_id}")
def delete_exercise(exercise_id: UUID, db: Session = Depends(get_db)):
    db_ex = crud.get_exercise_by_id(db, exercise_id)
    if not db_ex:
        raise HTTPException(status_code=404, detail="Übung nicht gefunden")

    crud.delete_exercise(db, exercise_id)
    return {"message": "Übung wurde erfolgreich gelöscht"}


# -----------------------------
# ÜBUNG AKTUALISIEREN
# -----------------------------
@app.put("/{exercise_id}", response_model=schemas.ExerciseRead)
def update_exercise(
    exercise_id: UUID,
    exercise: schemas.ExerciseCreate,
    db: Session = Depends(get_db)
):
    db_ex = crud.get_exercise_by_id(db, exercise_id)
    if not db_ex:
        raise HTTPException(status_code=404, detail="Übung nicht gefunden")

    updated_ex = crud.update_exercise(db, exercise_id, exercise)
    return updated_ex
>>>>>>> 0be12a57868a06cd9b7e823ed7fd36984d314e81
