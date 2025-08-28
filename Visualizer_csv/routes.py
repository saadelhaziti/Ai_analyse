from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from .tasks_csv.visualizer_csv import clean_csv_task, analyze_csv_task

router = APIRouter(prefix="/csv", tags=["csv"])

@router.get("/cleaner")
async def cleaner(input_path: str):
    task = clean_csv_task.delay(input_path)   # exécution asynchrone
    return {"task_id": task.id, "status": "Processing started"}

@router.get("/analyst/{project_guid}")
async def analyst(project_guid: str):
    task = analyze_csv_task.delay(project_guid)   # exécution asynchrone
    return {"task_id": task.id, "status": "Analysis started"}
