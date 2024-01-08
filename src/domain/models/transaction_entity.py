from sqlalchemy import Column,Integer,String,Boolean,Double,DateTime
from sqlalchemy.orm import relationship
from src.domain.models.base_entity import BaseEntity

class TransactionEntity(BaseEntity):
    
    __tablename__ = "transaction"
    
    id = Column(Integer,primary_key=True)
    
    transaction_id = Column(String(255))
    
    category = Column(String(255))
    
    subcategory = Column(String(255),default=None,nullable=True)
    
    type = Column(String(255))
    
    amount = Column(Boolean)
    
    status = Column(String(255))
    
    balance = Column(Double)
    
    currency = Column(String(255))
    
    reference = Column(String(255))
    
    description = Column(String(255))
    
    collected_at = Column(DateTime)
    
    observations = Column(String(255))
    
    accounting_date = Column(DateTime)
    
    internal_identification = Column(String(255))
    
    created_at = Column(DateTime)
    
    collected_at = Column(DateTime)
    
    merchant_id = Column(Integer)
    
    account_id = Column(Integer)
    
    account = relationship("AccountEntity",back_populates="transaction")