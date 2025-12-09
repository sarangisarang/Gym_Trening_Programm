from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime


# -------------------- VERKNÜPFUNGSTABELLE (WORKOUT_EXERCISES) --------------------
# Laut ERD: Die Tabelle, die Workouts und Exercises verbindet (Viele zu Viele).
class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    # Primärschlüssel-Kombination aus Fremdschlüsseln
    workout_id = Column(Integer, ForeignKey("workouts.id"), primary_key=True)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), primary_key=True)

    # Zusätzliche Spalten für die Übungsausführung
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(DECIMAL)

    # ORM-Beziehungen
    workout = relationship("Workout", back_populates="exercises_link")
    exercise = relationship("Exercise", back_populates="workouts_link")


# -------------------- BENUTZER (USER) --------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    # Beziehung zu Exercises (Eins-zu-Viele)
    exercises = relationship("Exercise", back_populates="owner")

    # ✅ KORREKTUR: Beziehung zu Workouts hinzugefügt (Löst den AttributeError in CRUD).
    workouts = relationship("Workout", back_populates="owner")


# -------------------- ÜBUNG (EXERCISE) --------------------
class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    muscle_group = Column(String)

    # Fremdschlüssel zum Benutzer (Owner)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="exercises")

    # Beziehung zur Verknüpfungstabelle
    workouts_link = relationship("WorkoutExercise", back_populates="exercise")


# -------------------- TRAINING (WORKOUT) --------------------
class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    # ✅ KORREKTUR: Fremdschlüssel zum Benutzer hinzugefügt (Laut ERD).
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="workouts")

    # Beziehung zur Verknüpfungstabelle
    exercises_link = relationship("WorkoutExercise", back_populates="workout")