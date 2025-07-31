from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgres:admin@db:5432/AI_agent"
# DATABASE_URL = "postgresql://postgres:5432@db:5432/AI_agent"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)