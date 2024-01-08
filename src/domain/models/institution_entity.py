from sqlalchemy import Integer,String,Column
from sqlalchemy.orm import relationship
from src.domain.models.base_entity import BaseEntity

class InstitutionEntity(BaseEntity):
    
    __tablename__ = "institution"
    
    id = Column(Integer,primary_key=True)
    
    name = Column(String(255))
    
    type = Column(String(255))
    
    account = relationship("AccountEntity",back_populates="institution")