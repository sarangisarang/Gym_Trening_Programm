from typing import Optional
from pydantic import BaseModel, ConfigDict
<<<<<<< HEAD
from datetime import datetime
from typing import Optional, List, Union

=======
from datetime import datetime, date
from uuid import UUID
>>>>>>> 0be12a57868a06cd9b7e823ed7fd36984d314e81

# -------------------- HILFS-SCHEMATA (Hilfsschichten für Beziehungen) --------------------
# Dieses Schema bildet die Verknüpfungstabelle 'WorkoutExercise' ab.
class WorkoutExerciseBase(BaseModel):
    # WICHTIG: Die exercise_id muss gesendet werden, um zu wissen, welche Übung gemeint ist.
    exercise_id: int
    sets: int  # Sets und Reps (Sätze und Wiederholungen) sind jetzt Pflicht.
    reps: int
    weight: float  # Das Gewicht, als float/decimal (Laut ERD).


class WorkoutExerciseRead(WorkoutExerciseBase):
    # Wenn wir die Daten aus der DB lesen, brauchen wir die Workout ID
    workout_id: int

    # NEU: Wir müssen die 'Read'-Klasse wieder zur Konfiguration hinzufügen
    model_config = ConfigDict(from_attributes=True)

class WorkoutExerciseCreate(BaseModel):
    workout_id: int
    exercise_id: int
    sets: int
    reps: int
    weight: float


# -------------------- ÜBUNG (EXERCISE) --------------------
# WICHTIG: Muss vor Workout definiert werden, da es dort referenziert wird.
class ExerciseBase(BaseModel):
    title: str
    muscle_group: str
    # HINWEIS: Laut ERD müsste hier noch die Beschreibung ('description') rein.


class ExerciseCreate(ExerciseBase):
    # WICHTIG: user_id muss gesendet werden, da es ein Fremdschlüssel ist (Laut models.py).
    user_id: int


class ExerciseRead(ExerciseBase):
    id: int
    user_id: int

    # NEU: Wir müssen die 'Read'-Klasse wieder zur Konfiguration hinzufügen
    model_config = ConfigDict(from_attributes=True)


# -------------------- TRAINING (WORKOUT) --------------------
class WorkoutBase(BaseModel):
    title: str
    description: Optional[str] = None  # Entspricht den Notizen im ERD.
    # WICHTIG: user_id muss gesendet werden, da es ein Fremdschlüssel ist (Laut models.py).
    user_id: int


class WorkoutCreate(WorkoutBase):
    # Wir können optional eine Liste von Übungen direkt beim Erstellen übergeben.
    exercises: Optional[List[WorkoutExerciseBase]] = None


class WorkoutRead(WorkoutBase):
    id: int
    created_at: datetime  # Wann wurde es erstellt?

    # Hier können wir die Liste der verknüpften Übungen abrufen (Relationship).
    exercises: List[WorkoutExerciseRead] = []

    model_config = ConfigDict(from_attributes=True)


# -------------------- BENUTZER (USER) --------------------
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
<<<<<<< HEAD
    id: int
    # Beziehungshalter (Relationship holders): Damit wir sehen, was dem Benutzer gehört.
    exercises: List[ExerciseRead] = []  # Liste der Exercises, die der User erstellt hat.
    workouts: List[WorkoutRead] = []  # Liste der Workouts, die der User erstellt hat.
=======
    id: UUID
>>>>>>> 0be12a57868a06cd9b7e823ed7fd36984d314e81

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )


<<<<<<< HEAD
# WICHTIG: Pydantic v2 muss manchmal die Abhängigkeiten neu aufbauen, wenn zirkuläre Referenzen bestehen.
UserRead.model_rebuild()
=======
# ---------------- EXERCISE ----------------
class ExerciseBase(BaseModel):
    title: str
    muscle_group: str

class ExerciseCreate(ExerciseBase):
    pass

class ExerciseRead(BaseModel):
    id: UUID
    title: str
    muscle_group: str
    user_id: UUID | None

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )


# ---------------- WORKOUT ----------------
class WorkoutCreate(BaseModel):
    user_id: UUID
    date: date
    notes: Optional[str]

    model_config = ConfigDict(
        arbitrary_types_allowed=True
    )

class WorkoutRead(BaseModel):
    id: UUID
    user_id: UUID
    date: datetime
    notes: Optional[str]
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )
>>>>>>> 0be12a57868a06cd9b7e823ed7fd36984d314e81
