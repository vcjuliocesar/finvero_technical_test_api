import pytest
import re
from datetime import datetime
from fastapi.testclient import TestClient
from sqlalchemy import inspect
from src.application.main import app
from src.domain.models.account_entity import AccountEntity
from src.infrastructure.config.memory_database import MemoryDatabase
from src.infrastructure.dtos.create_acccount_dto import CreateAccountDto
from src.infrastructure.exceptions.account_not_found_exception import AccountNotFoundException
from src.infrastructure.exceptions.invalid_account_id_exception import InvalidAccountIdException
from src.infrastructure.repositories.account_repository import AccountRepository
from src.service.account_service import AccountService

instance = MemoryDatabase()

engine = instance.get_engine()


@pytest.fixture
def memory_db():
    instance = MemoryDatabase()

    db = instance.get_session()

    try:

        yield db

    finally:

        db.close()


@pytest.fixture
def account_repository(memory_db):
    # Configurar la base de datos de pruebas o en memoria para AccountRepository
    return AccountRepository(db=memory_db)


@pytest.fixture(scope='function')
def account_service(account_repository):

    return AccountService(repository=account_repository)


@pytest.fixture()
def client() -> TestClient:

    return TestClient(app)


@pytest.fixture
def set_up(account_service):

    create_account = CreateAccountDto(
        account_id="cb753384-3742-45a1-82a4-f8958a9463ba",
        link="3eefa5b0-7af0-4632-a431-58c8ee401144",
        currency="MXN",
        category="CREDIT_CARD",
        type="Cuentas de efectivo",
        number="169",
        agency="3814042",
        internal_identification="8281086",
        public_identification_name="CREDIT_CARD_NUMBER",
        public_identification_value="593",
        name="Cartão crédito visa platinum",
        last_accessed_at=datetime.now(),
        balance_type="LIABILITY",
        bank_product_id="9067974",
        created_at="2024-01-05T06:41:02.170183Z",
        collected_at="2024-01-08T11:05:34.894254Z"
    )

    entity = account_service.create(create_account)

    yield entity

    account_service.delete(entity)


# def test_it_retun_an_exception_if_account_id_is_invalid(account_service):

#     with pytest.raises(InvalidAccountIdException):

#         account_service.find_by_id('invalid-acount-id')


def test_it_retun_an_exception_if_account_not_exists(account_service):

    with pytest.raises(AccountNotFoundException):

        account_service.find_by_id('123')
