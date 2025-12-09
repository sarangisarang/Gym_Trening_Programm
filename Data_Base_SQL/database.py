from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

<<<<<<< HEAD
SQLALCHEMY_DATABASE_URL = "sqlite:///./gym.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
=======
# ---------------------------------------------------------
# Datenbankkonfiguration (SQLite)
# ---------------------------------------------------------

# SQLite-Verbindungs-URL (lokale Datei: gym.db)
SQLALCHEMY_DATABASE_URL = "sqlite:///./gym.db"

# Erstellen der Engine
# Für SQLite muss 'check_same_thread' deaktiviert werden,
# da mehrere Threads gleichzeitig auf dieselbe Verbindung zugreifen können.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Erstellen einer SessionFactory:
# autocommit=False  → Änderungen werden erst nach commit() gespeichert
# autoflush=False   → verhindert automatisches Zwischenspeichern
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Basisklasse für alle ORM-Modelle
Base = declarative_base()


# ---------------------------------------------------------
# Abhängigkeitsfunktion für FastAPI
# ---------------------------------------------------------
>>>>>>> 0be12a57868a06cd9b7e823ed7fd36984d314e81
def get_db():
    """
    Liefert eine neue Datenbank-Session zurück.
    Diese Funktion wird als Dependency in FastAPI-Routen genutzt.
    Nach jeder Anfrage wird die Session automatisch geschlossen.

    Beispiel:
        def endpoint(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
