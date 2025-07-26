import pandas as pd
import duckdb
import requests
from typing import List, Dict
from DB_Save.controller.Minio_controller import Get_file_from_minio
from DB_Save.Models_save.Minio_forma_save import Froma_Minio

def run_queries_to_minio(
    csv_path: str,
    prompts: List[Dict]
):
    """
    Executes SQL queries from a list of prompt dicts on a CSV file using DuckDB,
    and uploads the result as CSV to MinIO using Froma_Minio and POST_file_in_Minio.
    
    Args:
        csv_path (str): Path to CSV file containing data.
        prompts (List[Dict]): List of prompt objects (must include 'request_sql' and 'title').
    """

    # Load CSV data
    try:
       file_stream, _ = Get_file_from_minio(csv_path)
       df = pd.read_csv(file_stream, encoding='utf-8')
    except Exception as e:
        print(f"Failed to read CSV: {e}")
        return

    # Register table as 'data' in DuckDB
    duckdb.register("data", df)

    # Execute each SQL query and upload result
    for prompt in prompts:
        try:
            print(f"Executing: {prompt['title']}")
            sql = prompt["request_sql"]
            result_df = duckdb.query(sql).to_df()

            # Convert result to CSV

            output_stream = Froma_Minio(result_df)
            output_filename = prompt["title"].replace(" ", "_").replace("/", "_") + ".csv"
            files = {"file": (output_filename, output_stream, "text/csv")}
            response = requests.post("http://127.0.0.1:8000/DB_Save/Save_in_to_Minio", files=files)
            # add url to prompt
            # prompt.a

        except Exception as e:
            raise ValueError(f"Error executing SQL query '{prompt['title']}': {str(e)}") from e
