from pydantic import BaseModel, EmailStr
from typing import List
from datetime import date

class ProjectBase(BaseModel):
    Project_name : str
    data_type : str
    data_url_clean : str
    data_prute_url : str
    metadata_url : str

class ProjectCreate(ProjectBase):
    guid_user: str

class ProjectOut(ProjectBase):
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name_comple: str
    phone: str
    email: EmailStr
    datenaissance: date

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    projects: List[ProjectOut] = []
    class Config:
        orm_mode = True