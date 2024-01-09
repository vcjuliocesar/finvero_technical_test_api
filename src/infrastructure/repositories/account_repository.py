from fastapi import Depends
from sqlalchemy.orm import Session
from src.domain.models.account_entity import AccountEntity
from src.infrastructure.config.connection import get_db
from src.infrastructure.repositories.interface.repositoty_interface import RepositoryInterface

class AccountRepository(RepositoryInterface):
    
    def __init__(self,db:Session = Depends(get_db)) -> None:
        
        self.db = db
        
    def create(self, account:AccountEntity) -> AccountEntity:
        
        self.db.add(account)
        
        self.db.commit()
        
        return account
    
    def find_by(self, criteria:dict)-> AccountEntity:
        
        return self.db.query(AccountEntity).filter_by(**criteria).first()
    
    def delete(self, account:AccountEntity) -> None:
        
        self.db.delete(account)
        
        self.db.commit()