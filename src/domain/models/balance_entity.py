from sqlalchemy import Integer,Column,Double
from sqlalchemy.orm import relationship
from src.domain.models.base_entity import BaseEntity

class BalanceEntity(BaseEntity):
    
    __tablename__ = "balance"
    
    id = Column(Integer,primary_key=True)
    
    current = Column(Double)
    
    available = Column(Double)
    
    account = relationship("AccountEntity",back_populates="balance")