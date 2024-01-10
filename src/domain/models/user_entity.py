from src.domain.models.base_entity import BaseEntity
from sqlalchemy import Integer,String,Column,Boolean
from sqlalchemy.orm import relationship

class UserEntity(BaseEntity):
    
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    
    name = Column(String(255))
    
    email = Column(String(255),unique=True) 
    
    password = Column(String(255))