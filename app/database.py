from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv


load_dotenv()

# get the data from .env

DATABASE_URL = os.getenv("DATABASE_URL")
# DATABASE_URL = "postgresql://postgres:lavalava@localhost/databaseManagement"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

