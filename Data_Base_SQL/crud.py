from uuid import UUID
from sqlalchemy.orm import Session
<<<<<<< HEAD
from . import models, schemas
from sqlalchemy.orm import joinedload # Für Eager Loading von Beziehungen


# -------------------- BENUTZER CRUD (USER CRUD) --------------------
def create_user(db: Session, user: schemas.UserCreate):
    """
    Erstellt einen neuen Benutzer in der Datenbank.
    """
=======
from Data_Base_SQL import models, schemas
from Data_Base_SQL.models import Workout
from Data_Base_SQL.schemas import WorkoutCreate


# ---------------- USER CRUD ----------------

def create_user(db: Session, user: schemas.UserCreate):
>>>>>>> 0be12a57868a06cd9b7e823ed7fd36984d314e81
    db_user = models.User(
        name=user.name,
        email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


<<<<<<< HEAD
def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Gibt alle Benutzer zurück und lädt ihre zugehörigen Workouts und Exercises (Eager Loading).
    """
    # Lade Workouts und Exercises im Voraus (joinedload)
    return db.query(models.User)\
             .options(joinedload(models.User.workouts))\
             .options(joinedload(models.User.exercises))\
             .offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    """
    Gibt einen einzelnen Benutzer anhand der ID zurück.
    """
    # Lade Workouts und Exercises für den einzelnen Benutzer.
    return db.query(models.User)\
             .filter(models.User.id == user_id)\
             .options(joinedload(models.User.workouts))\
             .options(joinedload(models.User.exercises))\
             .first()


# -------------------- WORKOUT CRUD (TRAINING CRUD) --------------------
# ✅ KORREKTUR: Explizite Zuweisung, um den TypeError zu vermeiden.
def create_workout(db: Session, workout: schemas.WorkoutCreate):
    """
    Erstellt ein neues Workout in der Datenbank.
    """
    db_workout = models.Workout(
        title=workout.title,
        description=workout.description,
        user_id=workout.user_id # user_id muss aus dem Schema kommen
    )
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout


def get_workouts(db: Session, skip: int = 0, limit: int = 100):
    """
    Gibt alle Workouts zurück.
    """
    return db.query(models.Workout).offset(skip).limit(limit).all()


def get_workout_by_id(db: Session, workout_id: int):
    """
    Gibt ein einzelnes Workout anhand der ID zurück.
    """
    return db.query(models.Workout).filter(models.Workout.id == workout_id).first()


# -------------------- EXERCISE CRUD (ÜBUNG CRUD) --------------------
def create_exercise(db: Session, exercise: schemas.ExerciseCreate):
    """
    Erstellt eine neue Übung in der Datenbank.
    """
=======
def get_users(db: Session):
    return db.query(models.User).all()


def get_user_by_id(db: Session, user_id: UUID):
    return db.query(models.User).filter(models.User.id == user_id).first()


# ---------------- EXERCISE CRUD ----------------

def create_exercise(db: Session, exercise: schemas.ExerciseCreate):
    db_ex = models.Exercise(
        title=exercise.title,
        muscle_group=exercise.muscle_group
    )
    db.add(db_ex)
    db.commit()
    db.refresh(db_ex)
    return db_ex


def get_exercises(db: Session):
    return db.query(models.Exercise).all()


def get_exercise_by_id(db: Session, exercise_id: UUID):
    return db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()


def create_exercise_for_user(db: Session, user_id: UUID, exercise: schemas.ExerciseCreate):
>>>>>>> 0be12a57868a06cd9b7e823ed7fd36984d314e81
    db_ex = models.Exercise(
        title=exercise.title,
        muscle_group=exercise.muscle_group,
        user_id=exercise.user_id # user_id muss aus dem Schema kommen
    )
    db.add(db_ex)
    db.commit()
    db.refresh(db_ex)
    return db_ex


<<<<<<< HEAD
def get_exercises(db: Session, skip: int = 0, limit: int = 100):
    """
    Gibt alle Übungen zurück.
    """
    return db.query(models.Exercise).offset(skip).limit(limit).all()


def get_exercise_by_id(db: Session, exercise_id: int):
    """
    Gibt eine einzelne Übung anhand der ID zurück.
    """
    return db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()


# -------------------- WORKOUT_EXERCISE CRUD --------------------
def create_workout_exercise(db: Session, item: schemas.WorkoutExerciseCreate):
    """
    Erstellt eine neue Zuordnung (Verbindung) zwischen Workout und Übung.
    """
    db_workout_exercise = models.WorkoutExercise(
        workout_id=item.workout_id,
        exercise_id=item.exercise_id,
        sets=item.sets,
        reps=item.reps,
        weight=item.weight
    )

    db.add(db_workout_exercise)
    db.commit()
    db.refresh(db_workout_exercise)

    return db_workout_exercise
=======
def get_exercises_by_user(db: Session, user_id: UUID):
    return db.query(models.Exercise).filter(models.Exercise.user_id == user_id).all()


def delete_exercise(db: Session, exercise_id: UUID):
    db_ex = db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()
    if db_ex:
        db.delete(db_ex)
        db.commit()


def update_exercise(db: Session, exercise_id: UUID, exercise: schemas.ExerciseCreate):
    db_ex = db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()
    if not db_ex:
        return None

    db_ex.title = exercise.title
    db_ex.muscle_group = exercise.muscle_group

    db.commit()
    db.refresh(db_ex)
    return db_ex


# ---------------- WORKOUT CRUD ----------------

def create_workout(db: Session, data: WorkoutCreate):
    workout = Workout(
        user_id=data.user_id,
        date=data.date,
        notes=data.notes
    )
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout
>>>>>>> 0be12a57868a06cd9b7e823ed7fd36984d314e81
