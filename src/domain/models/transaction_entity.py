from sqlalchemy import Column,Integer,String,Boolean,Double,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from src.domain.models.base_entity import BaseEntity

class TransactionEntity(BaseEntity):
    
    __tablename__ = "transaction"
    
    id = Column(Integer,primary_key=True)
    
    transaction_id = Column(String(255))
    
    category = Column(String(255))
    
    subcategory = Column(String(255),default=None,nullable=True)
    
    type = Column(String(255))
    
    amount = Column(Double)
    
    status = Column(String(255))
    
    balance = Column(Double)
    
    currency = Column(String(255))
    
    reference = Column(String(255))
    
    description = Column(String(255))
    
    collected_at = Column(DateTime)
    
    observations = Column(String(255),nullable=True,default=None)
    
    accounting_date = Column(DateTime)
    
    internal_identification = Column(String(255))
    
    created_at = Column(DateTime)
    
    account_id = Column(Integer,ForeignKey('account.id'),nullable=True,default=None)
    
    account = relationship("AccountEntity",back_populates="transaction")
    
    