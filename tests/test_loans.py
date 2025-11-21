import pytest
from app import create_app


def test_list_loans_empty(client):
    """Test listing loans when database is empty."""
    response = client.get('/api/loans')
    assert response.status_code == 200
    assert response.json == []

def test_create_loan(client):
    """Test creating a new loan."""
    payload = {
        "borrower_id": "user123",
        "amount": 1000.00,
        "currency": "USD",
        "term_months": 12,
        "interest_rate_apr": 5.0
    }
    response = client.post('/api/loans', json=payload)
    assert response.status_code == 201
    data = response.json
    assert data["borrower_id"] == "user123"
    assert data["status"] == "pending"
