from pydantic import Field
from typing import Optional
from src.infrastructure.schemas.base_transaction import BaseTransaction

class TransactionSchema(BaseTransaction):
    
    id:Optional[int] = Field(default=1)
    
    class Config:
            
        from_attributes = True