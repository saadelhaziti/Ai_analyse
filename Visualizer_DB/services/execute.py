import json
import psycopg2
import pandas as pd
import io
import os
from typing import List, Dict
from DB_Save.controller.Minio_controller import POST_file_in_Minio
from Visualizer_DB.services.fetch_save import load_db_config
from DB_Save.Models_save.Minio_forma_save import Froma_Minio

# def load_visualizations_from_file(file_name: str):
#     current_dir = os.path.dirname(__file__)  
#     file_path = os.path.join(current_dir, "..", file_name)  
#     file_path = os.path.abspath(file_path)

#     with open(file_path, "r", encoding="utf-8") as f:
#         return json.load(f)

# def save_visualizations_to_file(file_path: str, data: List[Dict]):
#     with open(file_path, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=2, ensure_ascii=False)

def execute_queries_and_store(
    visualizations: List[Dict],
    db_config_path: str,
    dir_path : str,
    project_guid : str
) -> List[Dict]:
    # Charger config DB
    db_config = load_db_config(db_config_path)

    # Connexion à PostgreSQL
    try:
        conn = psycopg2.connect(
        dbname=db_config["dbname"],
        user=db_config["user"],
        password=db_config["password"],
        host=db_config["host"],
        port=db_config.get("port", 5432)
        )
        cursor = conn.cursor()
    except Exception as e:
        print(f" Erreur de connexion à PostgreSQL : {e}")
        return []
    id =0
    visualizations_result = []
    for vis in visualizations:
        sql = vis.get("request_sql")
        if not sql:
            print(f" Pas de requête SQL pour la visualisation ID={vis.get('id')}")
            continue

        try:
        # Try to execute and fetch query result
            cursor.execute(sql)
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
        except Exception as e:
            print(f"❌ Failed to execute/fetch SQL for ID={vis.get('id')}: {e}")
            continue
        try:
            df = pd.DataFrame(rows, columns=columns)
            id +=1
            # Convertir en CSV en mémoire
            output_stream = Froma_Minio(df)

            # Nom du fichier
            title_safe = str(vis["title"]).replace(" ", "_").replace("/", "_")
            output_filename = f"{dir_path}/results/Id{id}_{title_safe}.csv"

            # Upload dans MinIO
            file_url = POST_file_in_Minio(output_stream, output_filename, "text/csv")

            # Ajout dans le dictionnaire JSON
            vis["result_url"] = file_url
            vis["Project_guid"] = project_guid
            visualizations_result.append(vis)
            print(f"Résultat ID={vis.get('id')} enregistré à {file_url}")

        except Exception as e:
            print(f" Erreur SQL ID={vis.get('id')} : {e}")

    cursor.close()
    conn.close()
    return visualizations_result


