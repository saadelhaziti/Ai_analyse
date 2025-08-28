from fastapi import APIRouter, Depends
from .tasks_DB.visualizer_DB import connect_db_task, generate_visualizations_task
from Models.db_credentials import DBCredentials

router = APIRouter(prefix="/db", tags=["db"])

@router.post("/connect/{guid_project}")
def connect_db_async(guid_project: str, credentials: DBCredentials):
    task = connect_db_task.delay(guid_project, credentials.dict())
    return {"task_id": task.id, "status": "started"}

@router.get("/generate-JSON/{guid_project}")
def generate_visualizations_async(guid_project: str):
    task = generate_visualizations_task.delay(guid_project)
    return {"task_id": task.id, "status": "started"}
