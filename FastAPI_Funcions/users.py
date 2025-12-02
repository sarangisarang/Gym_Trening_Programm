from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Data_Base_SQL.database import get_db
from Data_Base_SQL import crud, schemas

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
