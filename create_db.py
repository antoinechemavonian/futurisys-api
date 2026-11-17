import sqlite3
from datetime import datetime

# Ce script crée la base de données et insère un exemple (pour le mentor)
def init_db():
    print("Création de la base de données predictions.db...")
    conn = sqlite3.connect("predictions.db")
    cursor = conn.cursor()
    
    # Création de la table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prediction_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input_data TEXT,
        prediction TEXT,
        probability REAL
    )
    """)
    
    # Insertion d'un exemple (pour prouver que ça marche)
    cursor.execute("""
    INSERT INTO prediction_logs (input_data, prediction, probability)
    VALUES ('{"age": 35, "revenu_mensuel": 5000}', 'Non', 0.18)
    """)
    
    conn.commit()
    conn.close()
    print("Base de données initialisée avec succès !")

if __name__ == "__main__":
    init_db()
