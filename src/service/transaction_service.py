from src.domain.models.transaction_entity import TransactionEntity
from src.infrastructure.dtos.create_transaction_dto import CreateTransactionDto
from src.infrastructure.repositories.transaction_repository import TransactionRepository
from src.infrastructure.exceptions.transaction_not_found_exception import TransactionNotFoundException
from src.infrastructure.schemas import transaction_schema


class TransactionService:

    def __init__(self, repository: TransactionRepository) -> None:

        self.repository = repository

    def create(self, transaction) -> TransactionEntity:

        return self.repository.create(TransactionEntity(**transaction.model_dump()))

    def find_by_id(self, transaction_id: str) -> TransactionEntity:


        exists = self.find_by({'transaction_id': transaction_id})

        if not exists:

            raise TransactionNotFoundException()

        return exists

    def find_by(self, criteria: dict) -> TransactionEntity:

        return self.repository.find_by(criteria)

    def get(self):
        
        return self.repository.get()
    
    def delete(self, transaction: transaction_schema) -> None:

        return self.repository.delete(transaction)
