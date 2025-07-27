from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from users.services.database import SessionLocal
from users.Models import schemas
import  users.controller.User_controller as API_user
import  users.controller.Project_controller as API_project

Users = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@Users.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return API_user.create_user_controller(user, db)

@Users.get("/users/{guid}", response_model=schemas.UserOut)
def get_user(guid: str, db: Session = Depends(get_db)):
    user = API_user.get_user_controller(guid, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@Users.put("/users/{guid}", response_model=schemas.UserOut)
def update_user(guid: str, user: schemas.UserCreate, db: Session = Depends(get_db)):
    return API_user.update_user_controller(guid, user, db)

@Users.delete("/users/{guid}")
def delete_user(guid: str, db: Session = Depends(get_db)):
    API_user.delete_user_controller(guid, db)
    return {"message": "User deleted"}

@Users.post("/projects/", response_model=schemas.ProjectOut)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return API_project.create_project_controller(project, db)

@Users.get("/projects/{guid}", response_model=schemas.ProjectOut)
def get_project(guid: str, db: Session = Depends(get_db)):
    proj = API_project.get_project_controller(guid, db)
    if not proj:
        raise HTTPException(status_code=404, detail="Project not found")
    return proj

@Users.get("/projects/", response_model=list[schemas.ProjectOut])
def get_all_projects(db: Session = Depends(get_db)):
    return API_project.get_all_projects_controller(db)
@Users.put("/projects/{guid}", response_model=schemas.ProjectOut)
def update_project(guid: str, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return API_project.update_project_controller(guid, project, db)

@Users.delete("/projects/{guid}")
def delete_project(guid: str, db: Session = Depends(get_db)):
    API_project.delete_project_controller(guid, db)
    return {"message": "Project deleted"}