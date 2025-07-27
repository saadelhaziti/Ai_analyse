from sqlalchemy.orm import Session
from users.Models.model import  Project
from users.Models.schemas import ProjectCreate
def create_project(db: Session, project: ProjectCreate):
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_project(db: Session, guid: str):
    return db.query(Project).filter(Project.guid == guid).first()

def gets_all_projects(db: Session):
    return db.query(Project).all()

def update_project(db: Session, guid: str, project: ProjectCreate):
    db_project = get_project(db, guid)
    if db_project:
        for key, value in project.dict().items():
            setattr(db_project, key, value)
        db.commit()
        db.refresh(db_project)
        return db_project
    return None

def delete_project(db: Session, guid: str):
    proj = get_project(db, guid)
    db.delete(proj)
    db.commit()