from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import Dict, Any

objets = joblib.load("modele_attrition.joblib")
modele = objets["modele"]
colonnes = objets["colonnes"]
seuil = objets["seuil"]

app = FastAPI(title="API Attrition TechNova")

class EmployeInput(BaseModel):
    data: Dict[str, Any]

@app.get("/health")
def health():
    return {"status": "ok", "modele_charge": True}

@app.post("/predict")
def predict(employe: EmployeInput):
    try:
        input_dict = employe.data
        input_data = pd.DataFrame([input_dict])
        
        for col in colonnes:
            if col not in input_data.columns:
                # On met "0" pour les chiffres, et "Non" pour le texte
                input_data[col] = 0 
                
        input_data = input_data[colonnes]
        
        proba = modele.predict_proba(input_data)[:, 1][0]
        prediction = "Oui" if proba >= seuil else "Non"
        
        return {"prediction": prediction, "probabilite": float(proba)}
        
    except Exception as e:
        # Si ça plante, on renvoie l'erreur exacte pour comprendre !
        return {"erreur_interne": str(e)}
