from sqlalchemy import Column,Integer,Double,String,Date
from sqlalchemy.orm import relationship
from src.domain.models.base_entity import BaseEntity

class LoanDataEntity(BaseEntity):
    
    __tablename__ = "loan_data"
    
    id = Column(Integer,primary_key=True)
    
    credit_limit = Column(Double)
    
    cutting_date = Column(String(255))
    
    next_payment_date = Column(Date)
    
    minimum_payment = Column(Double)
    
    monthly_payment = Column(Integer)
    
    no_interest_payment = Column(Double)
    
    last_payment_date = Column(Date)
    
    last_period_balance = Column(Double)
    
    interest_rate = Column(Double)
    
    account = relationship("AccountEntity",back_populates="loan_data")
    