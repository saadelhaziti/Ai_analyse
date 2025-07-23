from modeles.db_credentials import DBCredentials
from servise.connection_db import try_connect_db
from fastapi.responses import JSONResponse
import json
import os

def connect_db_controller(credentials: DBCredentials):
    try:
        # Essayer de se connecter
        try_connect_db(credentials)

        # Définir le chemin du fichier
        path = "backend/Data/db_credentials.json"

        # Créer le dossier s'il n'existe pas
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Sauvegarde des infos dans le fichier
        with open(path, "w", encoding="utf-8") as f:
            json.dump(credentials.dict(), f, indent=4)

        return JSONResponse(content={"message": " Connexion avec succès"})

    except Exception as e:
        return JSONResponse(content={"error": f" Connexion échouée : {str(e)}"}, status_code=400)
