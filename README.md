# API de Prédiction d'Attrition - Futurisys (Projet 5)

Ce projet déploie le modèle de Machine Learning (Random Forest) développé lors du projet 4 via une API FastAPI.

##  Outils utilisés
- Python 3 / FastAPI
- Scikit-Learn / Pandas
- Pytest (Tests)
-  PostgreSQL (ou SQLite pour le POC)

##  Installation locale
1. Cloner le dépôt.
2. Installer les dépendances : `pip install -r requirements.txt`
3. Lancer l'API : `uvicorn app.main:app --reload`
4. Accéder à la documentation interactive : `http://localhost:8000/docs`

 ### Installation
```bash
git clone https://github.com/antoinechemavonian/futurisys-api.git
cd futurisys-api
pip install -r requirements.txt
```


##  Structure du projet
- `app/main.py` : Le code de l'API.
- `tests/test_api.py` : Les tests unitaires.
- `modele_attrition.joblib` : Le modèle entraîné.

- 
