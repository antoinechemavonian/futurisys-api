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

### Lancement de l'API
```bash
uvicorn app.main:app --reload
````

##  Modèle de données (Schéma BDD)
La base de données contient une table principale pour la traçabilité :
**Table `prediction_logs`** :
- `id` (Integer, Clé Primaire) : Identifiant unique de la requête.
- `input_data` (JSON) : Les données de l'employé envoyées à l'API.
- `prediction` (String) : La prédiction du modèle ("Oui" ou "Non").
- `probability` (Float) : La probabilité associée à la prédiction.

##  Sécurité et Authentification
- **Gestion des secrets** : Les identifiants de la base de données (DATABASE_URL) ne sont pas dans le code. Ils sont gérés via les *GitHub Secrets* et injectés lors du déploiement (CI/CD).
- **Sécurisation de l'API** : Dans un environnement de production, l'API est protégée par une clé d'authentification (`X-API-Key`) transmise dans le header des requêtes pour garantir que seuls les employés autorisés y accèdent.
- **Validation stricte** : L'utilisation de Pydantic empêche les injections de données malveillantes (rejet automatique avec erreur 422).

## 🌍 Environnements
Le projet gère deux environnements distincts :
- **Développement / Test** : Utilisation de SQLite pour les tests locaux et l'exécution sur Google Colab (léger et rapide).
- **Production** : Utilisation de PostgreSQL (configuré via les variables d'environnement) pour la scalabilité.
