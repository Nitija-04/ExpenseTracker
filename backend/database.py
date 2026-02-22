from sqlalchemy import create_engine
from sqlalchemy import create
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import urllib.parse

load_dotenv()

# Get Supabase credentials from dashboard → Settings → Database
SUPABASE_URL = os.getenv("SUPABASE_URL")  # https://pbdumqbjzuxnylfjmmkr.supabase.co
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")  # Your anon key

# Parse for postgres connection (from Supabase Dashboard → Settings → Database)
# Format: postgresql://postgres.[project_ref]:[password]@aws-0-[region].pooler.supabase.com:5432/postgres
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:[Afro@feb@2005]@db.pbdumqbjzuxnylfjmmkr.supabase.co:5432/postgres")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()