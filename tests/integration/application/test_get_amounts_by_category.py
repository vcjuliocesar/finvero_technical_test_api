import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from fastapi import status
from sqlalchemy import inspect
from src.application.main import app,startup_event
from src.domain.models.account_entity import AccountEntity
from src.domain.models.base_entity import BaseEntity
from src.domain.models.transaction_entity import TransactionEntity
from src.infrastructure.config.memory_database import MemoryDatabase


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
        
@pytest.fixture()
def client() -> TestClient:

    return TestClient(app)
    
    

@pytest.fixture()
def set_up(client: TestClient) -> None:

    response = client.post(
        "/api/v1/login", json={"email": "jhon.doe@example.com", "password": "MySecretPassword_123"})

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
    