import json
import psycopg2

def load_db_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def execute_sql_from_json_postgres(json_path, db_config_path, output_path):
    # Charger la configuration de la base
    db_config = load_db_config(db_config_path)

    # Charger les visualisations
    with open(json_path, 'r', encoding='utf-8') as f:
        visualizations = json.load(f)

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
        print(f" Erreur de connexion à la base de données PostgreSQL : {e}")
        return

    results = []

    for viz in visualizations:
        sql = viz.get("request_sql")
        title = viz.get("titre")
        print(f" Exécution de la requête : {title}")
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            rows_as_dict = [dict(zip(columns, row)) for row in rows]
            results.append({
                "id": viz.get("id"),
                "titre": title,
                "colonnes": columns,
                "résultats": rows_as_dict,
                "erreur": None
            })
        except Exception as e:
            print(f" Erreur dans '{title}' : {e}")
            results.append({
                "id": viz.get("id"),
                "titre": title,
                "colonnes": [],
                "résultats": [],
                "erreur": str(e)
            })

    cursor.close()
    conn.close()

    # Sauvegarde des résultats dans un fichier JSON
    try:
        with open(output_path, 'w', encoding='utf-8') as f_out:
            json.dump(results, f_out, indent=4, ensure_ascii=False)
        print(f"\n Résultats enregistrés dans : {output_path}")
    except Exception as e:
        print(f" Erreur lors de l'enregistrement du fichier JSON : {e}")

    return results

# Exemple d’utilisation
if __name__ == "__main__":
    execute_sql_from_json_postgres(
        json_path="../Data/output_visualizations.json",
        db_config_path="../modeles/db_credentials.json",
        output_path="../Data/output_results.json"
    )


# object mineao
# resultat json mongodb elasticsearch
# abstract class 2 functions save and retrieve
# minao + elasticsearch
# class interface