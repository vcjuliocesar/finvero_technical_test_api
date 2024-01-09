from fastapi import Depends
from sqlalchemy.orm import Session
from src.domain.models.transaction_entity import TransactionEntity
from src.infrastructure.config.connection import get_db
from src.infrastructure.repositories.interface.repositoty_interface import RepositoryInterface

class TransactionRepository(RepositoryInterface):
    
    def __init__(self,db:Session = Depends(get_db)) -> None:
        
        self.db = db
        
    def create(self, transaction:TransactionEntity) -> TransactionEntity:
        
        self.db.add(transaction)
        
        self.db.commit()
        
        return transaction
    
    def find_by(self, criteria:dict)-> TransactionEntity:
        
        return self.db.query(TransactionEntity).filter_by(**criteria).first()
    
    
    def get(self):
    
        return self.db.query(TransactionEntity).all()
    
    def delete(self, transaction:TransactionEntity) -> None:
        
        self.db.delete(transaction)
        
        self.db.commit()