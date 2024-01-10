from fastapi import Depends
from src.domain.models.user_entity import UserEntity as User
from src.infrastructure.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.infrastructure.exceptions.user_not_found_exception import UserNotFoundException
from src.infrastructure.repositories.user_repository import UserRepository
from src.infrastructure.schemas.user_schema import UserSchema
from src.infrastructure.utils.password_utils import PasswordUtils

class UserService:
    
    def __init__(self,user_repository:UserRepository = Depends()) -> None:
        
        self.user_repository = user_repository
    
    def get_all(self) -> list:
        
        return self.user_repository.get()
    
    def find_by_id(self,user_id:int):
        
        return self.user_repository.find_by_id(user_id)

    def find_by_email(self,user:User) -> User:
        
        return self.user_repository.find_by_email(user)
    
    def find_one(self,criteria:dict) -> list:
        
        return self.user_repository.find_one(criteria)
        
    def create(self,user:UserSchema) -> User:
        
        exist = self.user_repository.find_by_email(user)
        
        if exist:
            
            raise UserAlreadyExistsException()
        
        user.password = PasswordUtils().hash_password(user.password)
        
        return self.user_repository.create(User(**user.model_dump()))
    
    def update(self,user_id:int,user_data:UserSchema) -> User:
        
        user = self.user_repository.find_by_id(user_id)
        
        if not user:
            
             raise UserNotFoundException()
        
        user.name = user_data.name
        
        user.email = user_data.email
        
        user.password = user_data.password
        
        user.is_active = user_data.is_active
        
        user.is_admin = user_data.is_admin
        
        return self.user_repository.update(user)
    
    def delete(self,user_id:int) -> None:
        
        user = self.find_by_id(user_id)
        
        if not user:
            
            raise UserNotFoundException()
         
        return self.user_repository.delete(user)