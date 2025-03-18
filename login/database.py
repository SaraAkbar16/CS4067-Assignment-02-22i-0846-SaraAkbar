import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Correct DATABASE_URL based on docker-compose service "db"
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:sara2020@db:5432/users")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
