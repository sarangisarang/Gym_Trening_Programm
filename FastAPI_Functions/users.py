<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Data_Base_SQL import crud, schemas, database
from typing import List

# Definiere den Router für Benutzer
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Datenbank-Abhängigkeit (Dependency)
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------- POST (Neuen Benutzer Erstellen) --------------------
@router.post("/", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # ZUSATZPRÜFUNG: Man könnte hier prüfen, ob die E-Mail bereits existiert.
    return crud.create_user(db=db, user=user)


# -------------------- GET (Alle Benutzer Lesen) --------------------
@router.get("/", response_model=List[schemas.UserRead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # RUFEN: Alle Benutzer abrufen. Die CRUD-Funktion lädt bereits Workouts und Exercises (Eager Loading).
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# -------------------- GET (Einzelnen Benutzer Lesen) --------------------
@router.get("/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    # RUFEN: Einen spezifischen Benutzer anhand der ID abrufen
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
    return db_user
=======
from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.orm import Session
from Data_Base_SQL.database import get_db
from Data_Base_SQL import crud, schemas

app = APIRouter(prefix="/users", tags=["Benutzer"])


# -----------------------------
# BENUTZER ERSTELLEN
# -----------------------------
@app.post("/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_users = crud.get_users(db)

    for u in existing_users:
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="E-Mail existiert bereits")

    return crud.create_user(db, user)


# -----------------------------
# ALLE BENUTZER ANZEIGEN
# -----------------------------
@app.get("/", response_model=list[schemas.UserRead])
def list_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)

    if not users:
        raise HTTPException(status_code=404, detail="Keine Benutzer gefunden")

    return users


# -----------------------------
# BENUTZER NACH ID ABRUFEN (UUID!)
# -----------------------------
@app.get("/{user_id}", response_model=schemas.UserRead)
def get_user(user_id: UUID, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")

    return user
>>>>>>> 0be12a57868a06cd9b7e823ed7fd36984d314e81
