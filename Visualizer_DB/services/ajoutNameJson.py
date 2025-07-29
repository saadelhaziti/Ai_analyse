import json
from typing import List, Dict

def add_user_to_json_file(json_data: List[Dict], user_value: str) -> List[Dict]:
    """
    Ajoute ou met à jour l'attribut "project" dans chaque élément d'une liste JSON en mémoire.

    :param json_data: Liste d'objets JSON (déjà chargée en mémoire)
    :param user_value: Valeur à attribuer au champ "project"
    :return: La liste mise à jour
    """
    try:
        # 1. Vérifier que c'est une liste de dictionnaires
        if not isinstance(json_data, list):
            raise ValueError("Les données JSON doivent être une liste d'objets.")

        # 2. Ajouter ou mettre à jour le champ "project"
        for item in json_data:
            if isinstance(item, dict):
                item["project"] = user_value

        print('Le champ "project" a été ajouté à tous les objets.')
        return json_data

    except Exception as e:
        print(f"Erreur lors de la mise à jour des données : {e}")
        return json_data
