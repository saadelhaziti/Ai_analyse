from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from Visualizer_csv.controller.controller_cleaner import clean_data
from Visualizer_csv.controller.controller_analyst import analyze_controll
from users.services.database import SessionLocal
from sqlalchemy.orm import Session
from Visualizer_csv.services.execution_sql import run_queries_to_minio
from users.services.Project_Services import get_project
from Visualizer_DB.services.elasticsearch import ElasticsearchInterface
from Models.recom import generate_recommendation


app = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/cleaner")
async def cleaner(input_path: str):
    
    # Clean data and save in form csv
    try:
        result = clean_data(input_path)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})
    return JSONResponse(content={"message": result})

@app.get("/analyst/{project_guid}")
def analyst(project_guid: str,db: Session = Depends(get_db)):
    try:
        proj = get_project(db, project_guid)
        csv_path = proj.data_prute_url  # Assuming this is the path to the CSV file
        charts = analyze_controll(csv_path)
        if not charts:
            raise ValueError("No charts generated from the analysis.")
        # Save charts to a JSON file
        charts_finale = run_queries_to_minio(csv_path, charts, project_guid)
        generate_recommendation(project_guid, db)
        return charts_finale  # Let FastAPI handle the serialization
    except Exception as e:
        print(" Erreur interne :", str(e))
        return JSONResponse(status_code=500, content={"message": str(e)})
