import pytest
from fastapi.testclient import TestClient
from sqlalchemy import inspect
from src.application.main import app
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


def test_it_validates_the_creation_of_the_database_and_tables(client:TestClient,memory_db):
    
    inspector = inspect(engine)
    
    assert inspector.has_table('transaction')
    
    assert inspector.has_table('account')
    
    
    