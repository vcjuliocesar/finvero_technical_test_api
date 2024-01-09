from pydantic import BaseModel,Field
from typing import Optional


class UserPostRequest(BaseModel):
    
    name:str = Field("Jhon Doe",title="Name")
    
    email:str = Field("jhon.doe@example.com",title="Email")
    
    password:str = Field("MySecretPassword_123",title="Password")
    
class UserAuthRequest(BaseModel):
      
    email:str = Field("jhon.doe@example.com",title="Email")
    
    password:str = Field("MySecretPassword_123",title="Password")

class UserSchema(UserPostRequest):
    
    id:Optional[int] = Field(default=None)
    
    is_active:bool
    
    is_admin:bool
    
    class Config:
        
        from_attributes = True