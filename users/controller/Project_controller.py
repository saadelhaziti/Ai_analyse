from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from users.services.database import SessionLocal
from users.Models import schemas
import  users.services.User_Services as API_user
import  users.services.Project_Services as API_project

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_project_controller(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    # Validate project not empty
    if not project:
        raise HTTPException(status_code=400, detail="Project data is required")
    #the user must exist before creating a project
    if not API_user.get_user(db, project.guid_user):
        raise HTTPException(status_code=404, detail="User not found")
    return API_project.create_project(db, project)

def get_project_controller(guid: str, db: Session = Depends(get_db)):
    proj = API_project.get_project(db, guid)
    if not proj:
        raise HTTPException(status_code=404, detail="Project not found")
    return proj

def get_all_projects_controller(db: Session = Depends(get_db)):
    projects = API_project.gets_all_projects(db)
    if not projects:
        raise HTTPException(status_code=404, detail="No projects found")
    return projects
def update_project_controller(guid: str, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    # Validate project not empty
    if not project:
        raise HTTPException(status_code=400, detail="Project data is required")
    proj = API_project.get_project(db, guid)
    if not proj:
        raise HTTPException(status_code=404, detail="Project not found")
    updated_project = API_project.update_project(db, guid, project)
    if not updated_project:
        raise HTTPException(status_code=400, detail="Failed to update project")
    return updated_project  

def delete_project_controller(guid: str, db: Session = Depends(get_db)):
    proj = API_project.get_project(db, guid)
    if not proj:
        raise HTTPException(status_code=404, detail="Project not found")
    API_project.delete_project(db, guid)
    return {"message": "Project deleted"}
