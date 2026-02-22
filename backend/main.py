from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env

# Database imports (create these files next)
from database import engine, get_db
from models import Base, Expense

# Create tables (runs once)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API")

# Pydantic Schemas
class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str

class ExpenseResponse(ExpenseCreate):
    id: int
    
    class Config:
        from_attributes = True

@app.get("/")
def read_root():
    return {
        "message": "Expense Tracker API is live!",
        "supabase_url": os.getenv("SUPABASE_URL")[:20] + "..."
    }

@app.post("/expenses/", response_model=ExpenseResponse)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.get("/expenses/", response_model=List[ExpenseResponse])
def get_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).all()

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted successfully"}