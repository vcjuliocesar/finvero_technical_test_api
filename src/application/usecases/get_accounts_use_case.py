from fastapi import Depends
from src.service.account_service import AccountService

class GetAccountsUseCase:
    
    def __init__(self,account_service:AccountService = Depends()) -> None:
        self.account_service = account_service
        
    def execute(self):
        
        try:
            
            return self.account_service.get()
        
        except Exception as error:
        
            raise error