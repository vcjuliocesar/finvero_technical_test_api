# from fastapi import Depends
# from src.infrastructure.dtos.create_transaction_dto import CreateTransactionDto
# from src.service.transaction_service import TransactionService

# class TransactionUseCase:
    
#     def __init__(self,transaction_service:TransactionService = Depends()) -> None:
        
#         self.transaction_service = transaction_service
        
#     def execute(self,transaction:CreateTransactionDto):
        
#         try:
            
#             return self.user_service.create(transaction)
        
#         except Exception as error:
        
#             raise error