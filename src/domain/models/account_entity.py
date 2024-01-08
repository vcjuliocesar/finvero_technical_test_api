from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Integer,String,DateTime,Column,ForeignKey
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
    
    balance_id = Column(Integer,ForeignKey('balance.id'))
    
    credit_data_id = Column(Integer,ForeignKey('credit_data.id'),nullable=True,default=None)
    
    loan_data_id = Column(Integer,ForeignKey('loan_data.id'),nullable=True,default=None)
    
    institution_id = Column(Integer,ForeignKey('institution.id'),nullable=True,default=None)
    
    transaction_id = Column(Integer,ForeignKey('transaction.id'),nullable=True,default=None)
    
    created_at = Column(DateTime,default=datetime.now())
    
    collected_at = Column(DateTime,default=datetime.now())
    
    balance = relationship('BalanceEntity',back_populates='account')
    
    credit_data = relationship('CreditDataEntity',back_populates='account')
    
    loan_data = relationship('LoanDataEntity',back_populates='account')
    
    institution = relationship('InstitutionEntity',back_populates='account')
    
    transaction = relationship('TransactionEntity',back_populates='account')
    
    
    