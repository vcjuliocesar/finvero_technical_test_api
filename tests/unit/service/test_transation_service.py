import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from src.application.main import app
from src.domain.models.account_entity import AccountEntity
from src.infrastructure.config.memory_database import MemoryDatabase
from src.infrastructure.dtos.create_acccount_dto import CreateAccountDto
from src.infrastructure.dtos.create_transaction_dto import CreateTransactionDto
from src.infrastructure.repositories.account_repository import AccountRepository
from src.infrastructure.repositories.transaction_repository import TransactionRepository
from src.service.account_service import AccountService
from src.service.transaction_service import TransactionService

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
    
    return AccountRepository(db=memory_db)


@pytest.fixture()
def account_service(account_repository):

    return AccountService(repository=account_repository)

@pytest.fixture
def transaction_repository(memory_db):
    
    return TransactionRepository(db=memory_db)


@pytest.fixture()
def transaction_service(transaction_repository):

    return TransactionService(repository=transaction_repository)


@pytest.fixture()
def client() -> TestClient:

    return TestClient(app)


@pytest.fixture
def create_account(account_service):

    create_account_entity = CreateAccountDto(
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

    account_entity = account_service.create(create_account_entity)

    yield account_entity

    #account_service.delete(account_entity)
    
@pytest.fixture
def create_transaction(create_account,account_service,transaction_service):

    create_transaction= CreateTransactionDto(
        transaction_id="0644634a-696e-42df-95e1-c05772d9a6ab",
        category="Income & Payments",
        subcategory="test",
        type="INFLOW",
        amount="380.03",
        status="PROCESSED",
        balance="25645.5",
        currency="MXN",
        reference="1128",
        description="DISPERSION",
        collected_at="2024-01-07T21:55:58.681926Z",
        observations="null",
        accounting_date="2023-12-28T07:36:31",
        internal_identification="51d312e3",
        created_at="2023-12-28T07:36:31",
        account_id=create_account.id
        ) 

    entity = transaction_service.create(create_transaction)

    yield entity
    
    account_service.delete(create_account)
    
    transaction_service.delete(entity)

def test_create_transaction(create_transaction):

    pass