from fastapi import Depends
from src.infrastructure.schemas.user_schema import UserSchema as User
from src.domain.models.user_entity import UserEntity as User
from src.service.user_service import UserService

class FindByEmailUserUseCase:
    
    def __init__(self,user_service:UserService = Depends()) -> None:
        
        self.user_service = user_service
        
    def execute(self,user:User) -> User:
        
        try:
            
            return self.user_service.find_by_email(user)
        
        except Exception as error:
        
            raise error