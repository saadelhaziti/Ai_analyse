from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Visualizer_csv.controller.controller_cleaner import clean_data
from Visualizer_csv.controller.controller_analyst import analyze_controll
from Visualizer_csv.services.execution_sql import run_queries_to_minio
import json
import os

app = APIRouter()


@app.get("/cleaner")
async def cleaner(input_path: str):
    
    # Clean data and save in form csv
    try:
        result = clean_data(input_path)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})
    return JSONResponse(content={"message": result})
@app.get("/analyst")
def analyst(csv_path: str, output_path: str = "charts.json"):
    try:
        charts = analyze_controll(csv_path, output_path)
        return {"charts": charts}  # Let FastAPI handle the serialization
    except Exception as e:
        print(" Erreur interne :", str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})

@app.get("/execution_sql")
def execution_sql(csv_path: str, project_guid: str = None):
    """
    Execute SQL queries from prompts and upload results to MinIO.
    
    Args:
        csv_path (str): Path to the CSV file.
        prompts (list): List of prompt dictionaries containing 'request_sql' and 'title'.
    """
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, "charts.json")
        with open(json_path, "r") as f:
            prompts = json.load(f)
        run_queries_to_minio(csv_path, prompts, project_guid)
        return {"message": "SQL queries executed and results uploaded successfully."}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})

