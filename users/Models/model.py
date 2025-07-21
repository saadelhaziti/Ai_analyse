from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
import uuid
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()



class Project(Base):
    __tablename__ = 'project'
    guid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    guid_user = Column(String, ForeignKey('user.guid'))
    data_url_clean = Column(String)
    data_prute_url = Column(String)
    guid_elasticsearch = Column(String)

    user = relationship("User", back_populates="projects")

class User(Base):
    __tablename__ = 'user'
    guid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name_comple = Column(String)
    phone = Column(String)
    email = Column(String)
    datenaissance = Column(Date)
    hashed_password = Column(String)

    projects = relationship("Project", back_populates="user", cascade="all, delete")