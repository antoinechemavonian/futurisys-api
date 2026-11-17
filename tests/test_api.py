from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict_valid():
    payload = {"age": 35, "revenu_mensuel": 5000, "annees_dans_l_entreprise": 5}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_invalid():
    payload = {"age": "trente-cinq"} # Erreur : string au lieu d'int
    response = client.post("/predict", json=payload)
    assert response.status_code == 422 # FastAPI détecte l'erreur
