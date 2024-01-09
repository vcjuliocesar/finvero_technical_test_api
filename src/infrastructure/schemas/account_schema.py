from typing import Optional
from src.infrastructure.schemas.base_account import BaseAccount

class AccountSchema(BaseAccount):
    
    id:Optional[int]
    
    class Config:
            
        from_attributes = True
        
        allow_mutation = False