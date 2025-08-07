import pandas as pd, duckdb, json, os
from typing import List, Dict
from DB_Save.controller.Minio_controller import Get_file_from_minio, POST_file_in_Minio
from DB_Save.Models_save.Minio_forma_save import Froma_Minio
from Visualizer_DB.services.elasticsearch import ElasticsearchInterface

def run_queries_to_minio(
    csv_path: str,
    prompts: List[Dict],
    project_guid: str = None
):
    try:
        dir_path, _ = os.path.split(csv_path)
        file_stream, _ = Get_file_from_minio(csv_path)
        df = pd.read_csv(file_stream, encoding='utf-8')
    except Exception as e:
        print(f"Failed to read CSV: {e}")
        return []

    duckdb.register("data", df)
    save_path = f"{dir_path}/results/"
    valid_prompts = []
    id = 0

    es = ElasticsearchInterface(index_name="visualizations")

    for prompt in prompts:
        try:
            print(f"Executing: {prompt['title']}")
            sql = prompt["request_sql"]
            result_df = duckdb.query(sql).to_df()

            if len(result_df) < 1000:
                id += 1
                output_stream = Froma_Minio(result_df)
                title_safe = str(prompt["title"]).replace(" ", "_").replace("/", "_")
                output_filename = f"{save_path}Id{id}_{title_safe}.csv"

                file_url = POST_file_in_Minio(output_stream, output_filename, "text/csv")

                prompt["result_url"] = file_url
                prompt["Project_guid"] = project_guid
                prompt["id"] = id
                valid_prompts.append(prompt)

                es.save(prompt)
            else:
                print(f"Skipping '{prompt['title']}' – result has {len(result_df)} rows.")
                continue
        except Exception as e:
            print(f"Error executing SQL query '{prompt['title']}': {str(e)}")

    return valid_prompts

