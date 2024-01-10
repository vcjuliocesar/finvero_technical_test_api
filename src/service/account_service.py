from fastapi import Depends
from src.domain.models.account_entity import AccountEntity
from src.infrastructure.exceptions.invalid_account_id_exception import InvalidAccountIdException
from src.infrastructure.repositories.account_repository import AccountRepository
from src.infrastructure.dtos.create_acccount_dto import CreateAccountDto
from src.infrastructure.schemas.account_schema import AccountSchema
from src.infrastructure.exceptions.account_not_found_exception import AccountNotFoundException


class AccountService:

    def __init__(self, repository: AccountRepository = Depends()) -> None:

        self.repository = repository

    def create(self, account: CreateAccountDto) -> AccountEntity:

        return self.repository.create(AccountEntity(**account.model_dump()))

    def find_by_id(self, account_id: str) -> AccountEntity:

        # regex_uuid = r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"

        # is_valid = bool(re.match(regex_uuid, account_id))

        # if not is_valid:
            
        #     raise InvalidAccountIdException()

        exists = self.find_by({'account_id': account_id})

        if not exists:

            raise AccountNotFoundException()

        return exists

    def find_by(self, criteria: dict) -> AccountEntity:

        return self.repository.find_by(criteria)
    
    def get(self):
        
        return self.repository.get()

    def delete(self, account: AccountSchema) -> None:

        return self.repository.delete(account)
