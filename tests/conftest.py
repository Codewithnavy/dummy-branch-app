import pytest
from sqlalchemy import text
from app import create_app
from app.db import SessionContext

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def cleanup_database():
    """
    Fixture to clean up the database before and after each test.
    """
    # Cleanup before test
    with SessionContext() as session:
        session.execute(text("DELETE FROM loans"))
        session.commit()
    
    yield
    
    # Cleanup after test
    with SessionContext() as session:
        session.execute(text("DELETE FROM loans"))
        session.commit()
