from sqlalchemy import Column,String,Integer
from src.domain.models.base_entity import BaseEntity

class MerchantEntity(BaseEntity):
    
    __tablename__ = "merchant"
    
    id = Column(Integer,primary_key=True)
    
    name = Column(String(255))
    
    website = Column(String(255))
    
    logo = Column(String(255))