from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_predict():
    payload = {"data": {"age": 35, "revenu_mensuel": 5000.0}}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
