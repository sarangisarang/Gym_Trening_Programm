from fastapi import APIRouter
from Class_Funcions.Workout_Generator import WorkoutGenerator

router = APIRouter(prefix="/workout", tags=["Workout"])

@router.get("/{days}")
def generate_workout(days: int):
    generator = WorkoutGenerator()
    return generator.generate_plan(days)
