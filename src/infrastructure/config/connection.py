import sys
from src.infrastructure.config.database import Database
from src.infrastructure.config.memory_database import MemoryDatabase

def get_settings():
    
    return MemoryDatabase() if "pytest" in sys.modules else Database()


def get_db():
    
    instance = get_settings()
    
    db = instance.get_session()

    try:

        yield db

    finally:

        db.close()
