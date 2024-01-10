import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from fastapi import status
from sqlalchemy import inspect
from src.application.main import app,startup_event
from src.domain.models.account_entity import AccountEntity
from src.infrastructure.config.memory_database import MemoryDatabase


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
        
@pytest.fixture()
def client() -> TestClient:

    return TestClient(app)
    
    

@pytest.fixture()
def set_up(client: TestClient) -> None:

    response = client.post(
        "/api/v1/login", json={"email": "jhon.doe@example.com", "password": "MySecretPassword_123"})

    header = {"Authorization": f"Bearer {response.json()}"}
    
    yield header

def test_unauthorized_get_transactions(client:TestClient):
    
    header = {'Authorization': "Bearer {'message': 'Unauthorized'}"}
    
    response = client.get('/api/v1/transactions', headers=header)
    
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

def test_get_transactions(client:TestClient,set_up:set_up):
    
    header = set_up
    
    response = client.get('/api/v1/transactions', headers=header)
    
    print(response.status_code)

    assert response.status_code == status.HTTP_200_OK
    