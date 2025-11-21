

def test_get_stats_empty(client):
    """Test stats endpoint when database is empty."""
    response = client.get('/api/stats')
    assert response.status_code == 200
    data = response.json
    assert data["total_loans"] == 0
    assert data["total_amount"] == 0.0
