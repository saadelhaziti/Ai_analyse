from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Visualizer_csv.controller.controller_cleaner import clean_data
from Visualizer_csv.controller.controller_analyst import analyze_controll
from Visualizer_csv.services.execution_sql import run_queries_to_minio
from Visualizer_DB.services.elasticsearch import ElasticsearchInterface

app = APIRouter()


@app.get("/cleaner")
async def cleaner(input_path: str):
    
    # Clean data and save in form csv
    try:
        result = clean_data(input_path)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})
    return JSONResponse(content={"message": result})
@app.get("/analyst/{project_guid}")
def analyst(project_guid: str,csv_path: str):
    try:
        es = ElasticsearchInterface(index_name="visualizations")
        visualization = es.retrieve(project_guid)
        if visualization:
            return visualization
        charts = analyze_controll(csv_path)
        if not charts:
            raise ValueError("No charts generated from the analysis.")
        # Save charts to a JSON file
        charts_finale = run_queries_to_minio(csv_path, charts, project_guid)
        return charts_finale  # Let FastAPI handle the serialization
    except Exception as e:
        print(" Erreur interne :", str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})
