import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_SERVER = os.getenv("DB_SERVER")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")


DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_DATABASE}"

def get_db_engine():
    return create_engine(DB_URL)