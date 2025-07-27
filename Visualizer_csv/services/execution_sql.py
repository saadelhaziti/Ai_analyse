import pandas as pd, duckdb, json, os
from typing import List, Dict
from DB_Save.controller.Minio_controller import Get_file_from_minio, POST_file_in_Minio
from DB_Save.Models_save.Minio_forma_save import Froma_Minio

def run_queries_to_minio(
    csv_path: str,
    prompts: List[Dict],
    project_guid: str = None
):
    """
    Executes SQL queries from a list of prompt dicts on a CSV file using DuckDB,
    and uploads the result as CSV to MinIO using Froma_Minio and POST_file_in_Minio.

    Skips any result with more than 200 rows.
    Saves valid prompts into 'validjson.json'.
    """

    # Load CSV data
    try:
        dir_path, _ = os.path.split(csv_path)
        file_stream, _ = Get_file_from_minio(csv_path)
        df = pd.read_csv(file_stream, encoding='utf-8')
    except Exception as e:
        print(f"Failed to read CSV: {e}")
        return

    # Register table as 'data' in DuckDB
    duckdb.register("data", df)
    save_path = f"{dir_path}/results/"
    valid_prompts = []
    id = 0
    for prompt in prompts:
        try:
            print(f"Executing: {prompt['title']}")
            sql = prompt["request_sql"]
            result_df = duckdb.query(sql).to_df()

            if len(result_df) > 400:
                print(f"Skipping '{prompt['title']}' – result has {len(result_df)} rows.")
                continue
            id += 1
            output_stream = Froma_Minio(result_df)
            title_safe = str(prompt["title"]).replace(" ", "_").replace("/", "_")
            output_filename = f"{save_path}Id{id}_{title_safe}.csv"

            file_url = POST_file_in_Minio(output_stream, output_filename, "text/csv")
            prompt["result_url"] = file_url  # Add result URL to the prompt
            prompt["project_guid"] = project_guid  # Add project GUID to the prompt
            prompt["id"] = id
            valid_prompts.append(prompt)

        except Exception as e:
            print(f"Error executing SQL query '{prompt['title']}': {str(e)}")

    # Save valid prompts to JSON file
    try:
        with open("validjson.json", "w", encoding="utf-8") as f:
            json.dump(valid_prompts, f, ensure_ascii=False, indent=4)
        print("validjson.json saved successfully.")
    except Exception as e:
        print(f"Failed to save validjson.json: {e}")


