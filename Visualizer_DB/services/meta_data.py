import psycopg2
import pandas as pd
import numpy as np
import io
import os
from DB_Save.controller.Minio_controller import POST_file_in_Minio, Get_file_from_minio
from Visualizer_DB.services.fetch_save import load_db_config
from Visualizer_DB.services.sql import generate_complete_join_query

def meta_data(db_config_path: str, dir_path: str, schema_path: str):
    """
    Exécute une requête SQL, extrait des métadonnées, les sauvegarde sur MinIO, et retourne leur URL.

    Args:
        query (str): La requête SQL à exécuter.
        db_config (dict): Dictionnaire contenant les paramètres de connexion à PostgreSQL.
        output_path (str): Le chemin relatif où sauvegarder les métadonnées (dans MinIO).

    Returns:
        str: URL du fichier de métadonnées sauvegardé dans MinIO.
    """  
        # Connexion à la base
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
        # query = """SELECT *
        #             FROM products
        #             JOIN categories ON products.category_id = categories.category_id
        #             JOIN order_items ON order_items.product_id = products.product_id
        #             JOIN orders ON order_items.order_id = orders.order_id
        #             JOIN customers ON orders.customer_id = customers.customer_id
        #             JOIN payment_methods ON payment_methods.customer_id = customers.customer_id
        #             JOIN reviews ON reviews.product_id = products.product_id
        #             JOIN customers AS review_customers ON reviews.customer_id = review_customers.customer_id;
        #             """
        schema, _ = Get_file_from_minio(schema_path)
        if not schema:
            raise Exception("Schema file not found in MinIO.")
        schema_text = schema.read().decode('utf-8')
        query = generate_complete_join_query(schema_text)
        print(query)
        # Exécution de la requête
        cursor.execute(query)

        # Récupérer les noms des colonnes
        colnames = [desc[0] for desc in cursor.description]
        data = cursor.fetchall()

        # Fermer les connexions
        cursor.close()
        conn.close()

        # Vérification si vide
        if not data:
            return {"message": "Query returned no data."}

        # Convertir en DataFrame
        df = pd.DataFrame(data, columns=colnames)

        # Génération des métadonnées
        sample = df.head(5).to_string(index=False)
        columns = df.dtypes.astype(str).to_dict()
        unique_counts = df.nunique().sort_values(ascending=False).to_dict()
        corr_matrix = (
            df.select_dtypes(include=[np.number])
            .corr()
            .round(2)
            .to_dict()
        )

        metadata = (
            "Sample of data:\n" + sample + "\n\n" +
            "Columns:\n" + str(columns) + "\n\n" +
            "Unique counts:\n" + str(unique_counts) + "\n\n" +
            "Correlation matrix:\n" + str(corr_matrix)
        )

        
        metadata_stream = io.BytesIO(metadata.encode('utf-8'))
        metadata_stream.seek(0)

        file_url = POST_file_in_Minio(metadata_stream, dir_path, "text/plain")
        return file_url

    except Exception as e:
        print(f"Erreur lors de l'exécution ou génération de métadonnées : {e}")
        return {"error": str(e)}
