import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.infrastructure.config.database import Database


class MemoryDatabase(Database):
    
    def __init__(self):
        
        super().__init__()
        
        base_dir = os.path.dirname(os.path.realpath(__file__))
        
        dbname = f"{self.env().DATABASE_NAME}.sqlite"
        
        self.DATABASE_URL = f'sqlite:///{os.path.join(base_dir,dbname)}'
        
        self.engine = create_engine(self.DATABASE_URL,echo=True)
        
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=self.engine)
        
        