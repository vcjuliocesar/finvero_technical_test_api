from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.infrastructure.config.enviroment import get_enviroment_settinngs


class Database:

    def __init__(self):
        self.env = get_enviroment_settinngs()
        self.DATABASE_URL = f"{self.env().DATABASE_ENGINE}://{self.env().DATABASE_USER}:{self.env().DATABASE_PASSWORD}@{self.env().DATABASE_HOST}:{self.env().DATABASE_PORT}/{self.env().DATABASE_NAME}"
        self.engine = create_engine(self.DATABASE_URL, echo=True)
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

    def get_base(self):

        return self.Base

    def get_engine(self):

        return self.engine

    def get_session(self):
        
        return self.SessionLocal()
