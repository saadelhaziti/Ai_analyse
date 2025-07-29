from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgres:jhin2019@localhost:5432/AI_agent"
# DATABASE_URL = "postgresql://postgres:5432@localhost:5432/AI_agent"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)