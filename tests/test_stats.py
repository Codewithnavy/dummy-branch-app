import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_stats_empty(client):
    """Test stats endpoint when database is empty."""
    response = client.get('/api/stats')
    assert response.status_code == 200
    data = response.json
    assert data["total_loans"] == 0
    assert data["total_amount"] == 0.0
