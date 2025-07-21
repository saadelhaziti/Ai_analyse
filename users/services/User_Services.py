from sqlalchemy.orm import Session
from users.Models.model import User
from users.Models.schemas import UserCreate
from users.services.security import hash_password

def create_user(db: Session, user: UserCreate):
    db_user = User(
        name_comple=user.name_comple,
        phone=user.phone,
        email=user.email,
        datenaissance=user.datenaissance,
        hashed_password=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    
def update_user(db: Session, guid: str, user: UserCreate):
    db_user = get_user(db, guid)
    if not db_user:
        return None
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, guid: str):
    return db.query(User).filter(User.guid == guid).first()

# verify if user exists by email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def delete_user(db: Session, guid: str):
    user = get_user(db, guid)
    db.delete(user)
    db.commit()
