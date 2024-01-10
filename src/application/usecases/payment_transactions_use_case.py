from fastapi import Depends
from src.service.transaction_service import TransactionService

class PaymentTransactionsUseCase:
    
    def __init__(self,transaction_service:TransactionService = Depends()) -> None:
        self.transaction_service = transaction_service
        
        
    def execute(self):

        try:
            
            return self.transaction_service.find_by({'category':'Income & Payments'})
        
        except Exception as error:
        
            raise error