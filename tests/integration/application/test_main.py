import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from fastapi import status
from sqlalchemy import inspect
from src.application.main import app,startup_event
from src.domain.models.account_entity import AccountEntity
from src.domain.models.base_entity import BaseEntity
from src.domain.models.transaction_entity import TransactionEntity
from src.domain.models.user_entity import UserEntity
from src.infrastructure.config.memory_database import MemoryDatabase
from src.infrastructure.repositories.user_repository import UserRepository
from src.infrastructure.schemas.user_schema import UserSchema
from src.service.user_service import UserService


@pytest.fixture(scope="session", autouse=True)
def cleanup():
    
    db = MemoryDatabase()
    
    engine = db.get_engine()
        
    BaseEntity.metadata.create_all(bind=engine)
    
    yield
    
    BaseEntity.metadata.drop_all(bind=engine)
    

@pytest.fixture
def memory_db():
    instance = MemoryDatabase()
    
    db = instance.get_session()

    try:

        yield db
        
    finally:

        db.close()
        
@pytest.fixture
def user_repository(memory_db):
    # Configurar la base de datos de pruebas o en memoria para UserRepository
    return UserRepository(db=memory_db)

@pytest.fixture()
def user_service(user_repository):

    return UserService(user_repository=user_repository)
    
@pytest.fixture()
def client() -> TestClient:

    return TestClient(app)

@pytest.fixture()
def user(user_service):
    user_schema = UserSchema(
        name="Jhon Doe",
        email="jhon.doe@example.com",
        password="MySr3cr3tP4ssw0rd_123"
    )
    
    user_entity = user_service.create(user_schema)
    
    yield user_entity
    
    user_service.delete(user_entity.id)

@pytest.fixture()
def set_up(client: TestClient,user) -> None:
    
    response = client.post(
        "/api/v1/login", json={"email": "jhon.doe@example.com", "password":"MySr3cr3tP4ssw0rd_123"})

    header = {"Authorization": f"Bearer {response.json()}"}
    
    yield header


@pytest.fixture()
def account(memory_db):
    account_entity = AccountEntity(
            account_id="9cf598dc-3b6c-43e6-9c72-94b305d7837c",
            link="3eefa5b0-7af0-4632-a431-58c8ee401144",
            currency="MXM",
            category="LOAN_ACCOUNT",
            type="Créditos",
            number="15946701",
            agency="5760218",
            internal_identification="6379741",
            public_identification_name="ACCOUNT_NUMBER",
            public_identification_value="5333643",
            name="Cuenta nómina",
            last_accessed_at=datetime.now(),
            balance_type="LIABILITY",
            bank_product_id="4022243",
        )

    memory_db.add(account_entity)
    memory_db.commit()
    
    yield account_entity
    
    #memory_db.delete(account_entity)
    #memory_db.commit()
    
    
@pytest.fixture()
def transaction(memory_db,account):
    
    transaction_entity = TransactionEntity(
            transaction_id="0134ff16-37e5-4854-848a-67640c6f5043",
            category="Taxes",
            subcategory="null",
            type="OUTFLOW",
            amount="156.14",
            status="PROCESSED",
            balance="44018.72",
            currency="MXN",
            reference="4299",
            description="4299",
            #collected_at=item['collected_at'],
            observations="null",
            accounting_date=datetime.now(),
            internal_identification ="5573a287",
            #created_at=item['created_at'],
            account_id=account.id
            )
    
    transaction = memory_db.add(transaction_entity)
    memory_db.commit()
    yield transaction
    #memory_db.delete(transaction)
    #memory_db.commit()
    
    
def test_it_return_an_exception_if_user_is_not_exists_or_is_not_valid(client: TestClient):

    user = {"email": "fake_user@yopmail.com", "password": "123"}

    response = client.post('/api/v1/login', json=user)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
                    
def test_unauthorized_get_accounts(client:TestClient):
    
    header = {'Authorization': "Bearer {'message': 'Unauthorized'}"}
    
    
    response = client.get('/api/v1/accounts',headers=header)
    
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

def test_get_accounts(client:TestClient,set_up:set_up,account,transaction):
    
    header = set_up
    
    param = {"account_id":account.account_id}
    
    response = client.get('/api/v1/accounts', headers=header)
    
    assert response.status_code == status.HTTP_200_OK
    
    assert response.json() is not None
    
    data = response.json()
    
    assert data['results'][0]['account_id'] == "9cf598dc-3b6c-43e6-9c72-94b305d7837c"
    
def test_unauthorized_get_transactions(client:TestClient):
    
    header = {'Authorization': "Bearer {'message': 'Unauthorized'}"}
    
    response = client.get('/api/v1/transactions', headers=header)
    
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

def test_get_transactions(client:TestClient,set_up:set_up,transaction):
    
    header = set_up
    print("header",header)
    response = client.get('/api/v1/transactions', headers=header)
    
    print(response.status_code)

    assert response.status_code == status.HTTP_200_OK
    
    assert response.json() is not None
    
def test_unauthorized_get_amounts_by_category(client:TestClient):
    
    header = {'Authorization': "Bearer {'message': 'Unauthorized'}"}
    
    param = {"account_id":"9cf598dc-3b6c-43e6-9c72-94b305d7837c"}
    
    response = client.get('/api/v1/amounts_by_category',params=param, headers=header)
    
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    
def test_get_amounts_by_category(client:TestClient,set_up:set_up,account,transaction):
    
    header = set_up
    
    param = {"account_id":account.account_id}
    
    response = client.get('/api/v1/amounts_by_category',params=param, headers=header)
    
    assert response.status_code == status.HTTP_200_OK
    
    assert response.json() is not None
    
    
def test_unauthorized_get_balance(client:TestClient):
    
    header = {'Authorization': "Bearer {'message': 'Unauthorized'}"}
    
    param = {"account_id":"9cf598dc-3b6c-43e6-9c72-94b305d7837c"}
    
    response = client.get('/api/v1/balance',params=param, headers=header)
    
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

def test_get_balance(client:TestClient,set_up:set_up,account,transaction):
    
    header = set_up
    
    param = {"account_id":account.account_id}
    
    response = client.get('/api/v1/balance',params=param, headers=header)
    
    assert response.status_code == status.HTTP_200_OK
    
def test_unauthorized_get_income_and_expense_analysis(client:TestClient):
    
    header = {'Authorization': "Bearer {'message': 'Unauthorized'}"}
    
    param = {"account_id":"9cf598dc-3b6c-43e6-9c72-94b305d7837c"}
    
    response = client.get('/api/v1/income_and_expense_analysis',params=param, headers=header)
    
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

def test_get_income_and_expense_analysis(client:TestClient,set_up:set_up,account,transaction):
    
    header = set_up
    
    param = {"account_id":account.account_id}
    
    response = client.get('/api/v1/income_and_expense_analysis',params=param, headers=header)
    
    assert response.status_code == status.HTTP_200_OK
    
    assert response.json() is not None