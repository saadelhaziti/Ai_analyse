from sqlalchemy import Column, String, Date, ForeignKey, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from passlib.context import CryptContext
import uuid

# === DATABASE CONFIGURATION ===
DATABASE_URL = "postgresql://postgres:admin@db:5432/AI_agent"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# === PASSWORD HASHING SETUP ===
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# === DATABASE MODELS ===
class User(Base):
    __tablename__ = 'user'
    guid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name_comple = Column(String)
    phone = Column(String)
    email = Column(String)
    datenaissance = Column(Date)
    hashed_password = Column(String)

    projects = relationship("Project", back_populates="user", cascade="all, delete")


class Project(Base):
    __tablename__ = 'project'
    guid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    guid_user = Column(UUID(as_uuid=True), ForeignKey('user.guid'))
    Project_name = Column(String, nullable=False)
    data_type = Column(String, nullable=False)  # e.g., 'csv', 'json'
    data_url_clean = Column(String)
    data_prute_url = Column(String)
    metadata_url = Column(String)

    user = relationship("User", back_populates="projects")



# === CREATE ALL TABLES ===
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ All tables created successfully in PostgreSQL!")

if __name__ == '__main__':
    create_tables()  # Create tables fresh with the updated schema
