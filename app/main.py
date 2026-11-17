from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import Dict, Any
from sqlalchemy import create_engine, Column, Integer, String, Float, JSON
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# --- CHEMINS INTELLIGENTS (marche partout) ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "modele_attrition.joblib")
DB_PATH = os.path.join(BASE_DIR, "predictions.db")

# --- CONFIGURATION BASE DE DONNÉES ---
engine = create_engine(f"sqlite:///{DB_PATH}", connect_args={"check_same_thread": False})
Base = declarative_base()

class PredictionLog(Base):
    __tablename__ = "prediction_logs"
    id = Column(Integer, primary_key=True, index=True)
    input_data = Column(JSON)
    prediction = Column(String)
    probability = Column(Float)

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)

# --- CHARGEMENT DU MODÈLE ---
objets = joblib.load(MODEL_PATH)
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
    input_dict = employe.data
    input_data = pd.DataFrame([input_dict])
    
    for col in colonnes:
        if col not in input_data.columns:
            input_data[col] = 0 
            
    input_data = input_data[colonnes]
    
    proba = modele.predict_proba(input_data)[:, 1][0]
    prediction = "Oui" if proba >= seuil else "Non"
    
    db = SessionLocal()
    log = PredictionLog(
        input_data=input_dict,
        prediction=prediction,
        probability=float(proba)
    )
    db.add(log)
    db.commit()
    db.close()
    
    return {"prediction": prediction, "probabilite": float(proba)}
