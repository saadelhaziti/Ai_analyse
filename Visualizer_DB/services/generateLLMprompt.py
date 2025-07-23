import psycopg2
import os

def generate_llm_prompt_from_credentials(credentials: dict, output_path="../Data/schema_prompt.txt") -> str:
    # Connexion à la base
    conn = psycopg2.connect(
        dbname=credentials["dbname"],
        user=credentials["user"],
        password=credentials["password"],
        host=credentials["host"],
        port=credentials["port"]
    )
    cursor = conn.cursor()

    # Colonnes
    cursor.execute("""
        SELECT table_name, column_name, data_type, is_nullable
        FROM information_schema.columns
        WHERE table_schema = 'public'
        ORDER BY table_name, ordinal_position;
    """)
    columns_data = cursor.fetchall()

    # Clés étrangères
    cursor.execute("""
        SELECT
            tc.table_name AS table,
            kcu.column_name AS column,
            ccu.table_name AS foreign_table,
            ccu.column_name AS foreign_column
        FROM 
            information_schema.table_constraints AS tc 
        JOIN information_schema.key_column_usage AS kcu
          ON tc.constraint_name = kcu.constraint_name
        JOIN information_schema.constraint_column_usage AS ccu
          ON ccu.constraint_name = tc.constraint_name
        WHERE 
            constraint_type = 'FOREIGN KEY';
    """)
    foreign_keys = cursor.fetchall()
    conn.close()

    # Organisation des colonnes
    schema = {}
    for table, column, dtype, nullable in columns_data:
        schema.setdefault(table, []).append({
            "column": column,
            "type": dtype,
            "nullable": nullable
        })

    # Relations
    relations = []
    for table, column, foreign_table, foreign_column in foreign_keys:
        relations.append({
            "from_table": table,
            "from_column": column,
            "to_table": foreign_table,
            "to_column": foreign_column
        })

    # Construction du prompt
    prompt = "Voici le schéma de la base de données :\n\n"
    for table, columns in schema.items():
        prompt += f"Table {table}:\n"
        for col in columns:
            prompt += f"  - {col['column']} ({col['type']})"
            if col["nullable"] == "NO":
                prompt += " [NOT NULL]"
            prompt += "\n"
        prompt += "\n"

    prompt += "Relations entre les tables (clés étrangères) :\n"
    for rel in relations:
        prompt += f"  - {rel['from_table']}.{rel['from_column']} → {rel['to_table']}.{rel['to_column']}\n"

    prompt += "\nDescriptions des relations :\n"
    for rel in relations:
        prompt += (
            f"  - La table `{rel['from_table']}` contient une colonne `{rel['from_column']}` "
            f"qui fait référence à la colonne `{rel['to_column']}` de la table `{rel['to_table']}`.\n"
        )

    # Enregistrement automatique dans un fichier
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(prompt)

    return prompt
