import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_list_loans_empty(client):
    """Test listing loans when database is empty."""
    response = client.get('/api/loans')
    assert response.status_code == 200
    assert response.json == []
