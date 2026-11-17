from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Chargement du modèle et de ses métadonnées
objets = joblib.load("modele_attrition.joblib")
modele = objets["modele"]
colonnes = objets["colonnes"]
seuil = objets["seuil"]

app = FastAPI(title="API Attrition TechNova")

# Définition de ce que l'API attend en entrée
class EmployeInput(BaseModel):
    age: int
    revenu_mensuel: float
    annees_dans_l_entreprise: int

@app.get("/health")
def health():
    return {"status": "ok", "modele_charge": True}

@app.post("/predict")
def predict(employe: EmployeInput):
    # 1. On crée un dictionnaire avec toutes les colonnes requises initialisées à 0
    donnees_completes = {col: 0 for col in colonnes}

    # 2. On injecte les valeurs reçues via l'API
    donnees_completes["age"] = employe.age
    donnees_completes["revenu_mensuel"] = employe.revenu_mensuel
    donnees_completes["annees_dans_l_entreprise"] = employe.annees_dans_l_entreprise

    # 3. On crée le DataFrame avec la structure exacte attendue par le modèle
    input_data = pd.DataFrame([donnees_completes])[colonnes]

    # Prédiction
    proba = modele.predict_proba(input_data)[:, 1][0]
    prediction = "Oui" if proba >= seuil else "Non"

    return {"prediction": prediction, "probabilite": float(proba)}
