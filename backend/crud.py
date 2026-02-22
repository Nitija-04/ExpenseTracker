from sqlalchemy.orm import Session
from models import User, Expense
from schemas import UserCreate, ExpenseCreate
import hashlib

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_expense(db: Session, expense: ExpenseCreate, user_id: int):
    db_expense = Expense(**expense.dict(), owner_id=user_id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expenses(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Expense).filter(Expense.owner_id == user_id).offset(skip).limit(limit).all()
