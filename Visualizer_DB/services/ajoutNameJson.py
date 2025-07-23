import json

def add_user_to_json_file(file_path: str, user_value: str):
    """
    Ajoute ou met à jour l'attribut "user" dans chaque élément d'une liste JSON.

    :param file_path: Chemin du fichier JSON
    :param user_value: Valeur à attribuer au champ "user"
    """
    try:
        # 1. Charger le fichier JSON
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 2. Vérifier que c'est une liste de dictionnaires
        if not isinstance(data, list):
            raise ValueError("Le fichier JSON doit contenir une liste d'objets.")

        # 3. Ajouter ou mettre à jour le champ "user"
        for item in data:
            if isinstance(item, dict):
                item["project"] = user_value

        # 4. Sauvegarder les modifications dans le fichier
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f'Le champ "user" a été ajouté à tous les objets dans {file_path}.')

    except Exception as e:
        print(f"Erreur lors de la mise à jour du fichier : {e}")

