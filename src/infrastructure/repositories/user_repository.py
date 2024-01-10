from fastapi import Depends
from sqlalchemy.orm import Session
from src.domain.models.user_entity import UserEntity as User
from src.infrastructure.config.connection import get_db
from src.infrastructure.repositories.interface.repositoty_interface import RepositoryInterface

class UserRepository(RepositoryInterface):
    
    def __init__(self,db:Session = Depends(get_db)) -> None:
        
        self.db = db
    
    def find_by_id(self,user_id:int) -> User:
        
        return self.db.query(User).filter(User.id == user_id).first()
    
    def find_by_email(self,user:User) -> User:
        
        return self.db.query(User).filter(User.email == user.email).first()
    
    def find_one(self,criteria:dict) -> User:
        
        return self.db.query(User).filter_by(**criteria).first()
    
    def get(self) -> list:
        
        return self.db.query(User).all()
    
    def create(self,user:User) -> User:
        
        self.db.add(user)
        
        self.db.commit()
        
        return user
    
    def update(self, user:User) -> User:
        
        self.db.commit()
        
        self.db.refresh(user)
        
        return user
    
    def delete(self,user:User) -> None:
        
        self.db.delete(user)
        
        self.db.commit()
        
    def find_by(self, criteria:dict)-> User:
        
        return self.db.query(User).filter_by(**criteria).first()