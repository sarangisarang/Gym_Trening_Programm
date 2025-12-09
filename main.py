from fastapi import FastAPI
from Data_Base_SQL.database import engine
from Data_Base_SQL import models
from FastAPI_Functions import users, exercises, workout, workout_exercises

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inkludiert die Router-Objekte aus den Funktionsmodulen.
app.include_router(users.router)
app.include_router(exercises.router) 
app.include_router(workout.router)
app.include_router(workout_exercises.router)

@app.get("/")
def home():
    return {"message": "TEAM3 - Gym API is running!"}