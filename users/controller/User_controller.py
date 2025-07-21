from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from users.services.database import SessionLocal
from users.Models import schemas
import  users.services.User_Services as API_user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#controller for users and projectsfrom fastapi import APIRouter, Depends, HTTPException

def create_user_controller(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    # Validate user not empty
    if not user:
        raise HTTPException(status_code=400, detail="User data is required")
    
    # Check if user already exists
    existing_user = API_user.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    return API_user.create_user(db, user)

#updated controller functions for users and projects
def update_user_controller(guid: str, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = API_user.get_user(db, guid)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Validate user data
    if not user.name_comple or not user.email:
        raise HTTPException(status_code=400, detail="Name and email are required")
    
    return API_user.update_user(db, guid, user)

# Controller functions for getting and deleting users and projects
def get_user_controller(guid: str, db: Session = Depends(get_db)):
    user = API_user.get_user(db, guid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def delete_user_controller(guid: str, db: Session = Depends(get_db)):
    user = API_user.get_user(db, guid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    API_user.delete_user(db, guid)
    return {"message": "User deleted"}