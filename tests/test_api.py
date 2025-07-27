from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_random_quote():
    response = client.get("/quote")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data and "author" in data and "quote" in data

def test_get_all_quotes():
    response = client.get("/all_quotes")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 100 # quotes are hardcoded to 100

def test_get_quote_by_id():
    response = client.get("/quote/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

    response_404 = client.get("/quote/1000")
    assert response.status_code == 404