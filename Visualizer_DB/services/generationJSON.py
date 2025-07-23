from fastapi import FastAPI
import requests
import json
import os
from Visualizer_DB.services.ajoutNameJson import add_user_to_json_file 



def clean_llm_output(text: str) -> str:
    """Nettoie la réponse LLM en essayant d'extraire un JSON valide."""
    try:
        start = text.index('[')
        end = text.rindex(']') + 1
        return text[start:end]
    except ValueError:
        return text

def generate_json_via_llm(schema_txt_path: str, output_json_path: str, openrouter_api_key: str, user_value: str) -> list:
    # Lire le schéma
    with open(schema_txt_path, "r", encoding="utf-8") as f:
        schema_content = f.read()

    # Préparer le prompt
    prompt = (
        "Génère une liste de 10 objets JSON représentant des dashboards intelligents. "
        "Chaque objet doit contenir les clés suivantes :\n"
        "- id\n"
        "- title\n"
        "- columns\n"
        "- description\n"
        "- request_sql\n"
        "- suggested_chart\n\n"
        f"Voici le schéma de la base de données :\n{schema_content}"
    )

    headers = {
        "Authorization": f"Bearer {openrouter_api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/ministral-8b",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 2000,
        "temperature": 0.7
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"Erreur API : {response.status_code} - {response.text}")

    content = response.json()["choices"][0]["message"]["content"]
    print("Contenu reçu :\n", content)

    try:
        cleaned_content = clean_llm_output(content)
        generated_json = json.loads(cleaned_content)
    except Exception as e:
        raise Exception(f"Erreur de parsing JSON : {e}")

    # Sauvegarder le JSON dans le fichier
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(generated_json, f, indent=2, ensure_ascii=False)

    #Ajouter le champ "user" à chaque objet JSON
    add_user_to_json_file(output_json_path, user_value)

    return generated_json

