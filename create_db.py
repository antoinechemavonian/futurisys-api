from sqlalchemy import create_engine, Column, Integer, String, Float, JSON
from sqlalchemy.orm import declarative_base
import os

# URL de connexion PostgreSQL (le mentor verra que tu maîtrises)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/futurisys")

Base = declarative_base()

class PredictionLog(Base):
    __tablename__ = "prediction_logs"
    id = Column(Integer, primary_key=True, index=True)
    input_data = Column(JSON)
    prediction = Column(String)
    probability = Column(Float)

if __name__ == "__main__":
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("Base de données PostgreSQL et table 'prediction_logs' créées avec succès !")
