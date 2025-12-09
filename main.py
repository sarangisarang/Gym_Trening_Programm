from fastapi import FastAPI
from Data_Base_SQL.database import engine
from Data_Base_SQL import models
<<<<<<< HEAD
from FastAPI_Functions import users, exercises, workout, workout_exercises
=======
from FastAPI_Functions import users, exercises, workout

>>>>>>> 0be12a57868a06cd9b7e823ed7fd36984d314e81

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

<<<<<<< HEAD
# Inkludiert die Router-Objekte aus den Funktionsmodulen.
app.include_router(users.router)
app.include_router(exercises.router) 
app.include_router(workout.router)
app.include_router(workout_exercises.router)
=======
# Register routers
app.include_router(users.app)
app.include_router(exercises.app)
app.include_router(workout.app)

>>>>>>> 0be12a57868a06cd9b7e823ed7fd36984d314e81

@app.get("/")
def home():
    return {"message": "TEAM3 - Gym API is running!"}