from fastapi import Depends
from src.domain.models.transaction_entity import TransactionEntity
from src.infrastructure.dtos.create_transaction_dto import CreateTransactionDto
from src.infrastructure.exceptions.account_not_found_exception import AccountNotFoundException
from src.infrastructure.repositories.transaction_repository import TransactionRepository
from src.infrastructure.exceptions.transaction_not_found_exception import TransactionNotFoundException
from src.infrastructure.schemas import transaction_schema


class TransactionService:

    def __init__(self, repository: TransactionRepository = Depends()) -> None:

        self.repository = repository
        
    def create(self, transaction) -> TransactionEntity:

        return self.repository.create(TransactionEntity(**transaction.model_dump()))

    def find_by_id(self, transaction_id: str) -> TransactionEntity:


        exists = self.find_one_by({'transaction_id': transaction_id})

        if not exists:

            raise TransactionNotFoundException()

        return exists

    def find_by(self, criteria: dict) -> TransactionEntity:

        return self.repository.find_by(criteria)

    def get(self):
        
        return self.repository.get()
    
        
    def delete(self, transaction: transaction_schema) -> None:

        return self.repository.delete(transaction)

    def get_income_and_expense(self,account_id):
        
        return self.repository.get_income_and_expense(account_id)
    
    def get_balance(self,account_id):
        
        exists = self.repository.find_one_by_account_id(account_id)

        if not exists:
            
            raise AccountNotFoundException()
        
        return self.repository.get_balance(account_id)