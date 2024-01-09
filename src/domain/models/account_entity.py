from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Integer,String,DateTime,Column
from src.domain.models.base_entity import BaseEntity


class AccountEntity(BaseEntity):
    
    __tablename__ = "account"
    
    id = Column(Integer, primary_key=True)
    
    account_id = Column(String(255))
    
    link = Column(String(255))
    
    currency = Column(String(255))
    
    category = Column(String(255))
    
    type = Column(String(255))
    
    number = Column(String(255))
    
    agency = Column(String(255))
    
    internal_identification = Column(String(255))
    
    public_identification_name = Column(String(255))
    
    public_identification_value = Column(String(255))
    
    name = Column(String(255))
    
    last_accessed_at = Column(DateTime)
    
    balance_type = Column(String(255))
    
    bank_product_id = Column(String(255))
    
    created_at = Column(DateTime,default=datetime.now())
    
    collected_at = Column(DateTime,default=datetime.now())
    
    transaction = relationship('TransactionEntity',back_populates='account')
    
    
    