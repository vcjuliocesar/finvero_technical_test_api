import sys
from src.infrastructure.config.database import Database
from src.infrastructure.config.memory_database import MemoryDatabase

def get_settings():
    
    return MemoryDatabase() if "pytest" in sys.modules else Database()


def get_db():
    
    selected_db = get_settings()
    
    db_session = selected_db.get_session()

    try:

        yield db_session

    finally:

        db_session.close()
