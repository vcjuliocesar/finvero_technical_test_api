import sys
from src.infrastructure.config.connection import get_settings

db = get_settings()

engine = db.get_engine()

BaseEntity = db.get_base()

def init():
    
    if 'pytest' in sys.modules:
        
        BaseEntity.metadata.drop_all(bind=engine)
        
    BaseEntity.metadata.create_all(bind=engine)