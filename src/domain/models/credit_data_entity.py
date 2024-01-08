from datetime import datetime
from sqlalchemy import Integer,String,Column,DateTime,Date,Double
from sqlalchemy.orm import relationship
from src.domain.models.base_entity import BaseEntity

class CreditDataEntity(BaseEntity):
    
    __tablename__ = "credit_data"
    
    id = Column(Integer,primary_key=True)
    
    collected_at = Column(DateTime,default=datetime.now())
    
    credit_limit = Column(Double)
    
    cutting_date = Column(Date)
    
    next_payment_date = Column(Date)
    
    minimum_payment = Column(Double)
    
    monthly_payment = Column(Integer)
    
    no_interest_payment = Column(Double)
    
    last_payment_date = Column(Date)
    
    last_period_balance = Column(Double)
    
    interest_rate = Column(Double)
    
    account = relationship("AccountEntity",back_populates="credit_data")
    
    
    