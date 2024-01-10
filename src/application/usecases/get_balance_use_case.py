from fastapi import Depends
from src.service.transaction_service import TransactionService

class GetBalanceUseCase:
    def __init__(self,transaction_service:TransactionService = Depends()) -> None:
        self.transaction_service = transaction_service
        
        
    def execute(self,id:str):

        try:
            
            return self.transaction_service.get_balance(id)
        
        except Exception as error:
        
            raise error