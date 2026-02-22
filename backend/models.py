from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base  # Relative import

DATABASE_URL = "postgresql://[user]:[pass]@db.[project].supabase.co:5432/postgres"  # Your Supabase URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()