from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from typing import List
import crud, models, schemas
from database import SessionLocal, engine, Base

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ExpenseTracker API")

security = HTTPBasic()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/expenses/", response_model=schemas.Expense)
def create_expense(
    expense: schemas.ExpenseCreate,
    credentials: HTTPBasicCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_email(db, credentials.username)
    if not user or user.hashed_password != hashlib.sha256(credentials.password.encode()).hexdigest():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return crud.create_expense(db=db, expense=expense, user_id=user.id)

@app.get("/expenses/", response_model=List[schemas.Expense])
def read_expenses(
    skip: int = 0, limit: int = 100,
    credentials: HTTPBasicCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_email(db, credentials.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    expenses = crud.get_expenses(db=db, user_id=user.id, skip=skip, limit=limit)
    return expenses

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
