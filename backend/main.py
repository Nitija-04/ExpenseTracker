from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from . import models, database

# This line creates the tables in Supabase automatically if they don't exist
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Expense Tracker API")

# --- Pydantic Schemas (Data Validation) ---
class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str

class ExpenseResponse(ExpenseCreate):
    id: int
    
    class Config:
        from_attributes = True

# --- API Routes ---

@app.get("/")
def read_root():
    return {"message": "Expense Tracker API is live!"}

# Create a new expense
@app.post("/expenses/", response_model=ExpenseResponse)
def create_expense(expense: ExpenseCreate, db: Session = Depends(database.get_db)):
    db_expense = models.Expense(
        title=expense.title, 
        amount=expense.amount, 
        category=expense.category
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

# Get all expenses
@app.get("/expenses/", response_model=List[ExpenseResponse])
def get_expenses(db: Session = Depends(database.get_db)):
    return db.query(models.Expense).all()

# Delete an expense
@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(database.get_db)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted successfully"}