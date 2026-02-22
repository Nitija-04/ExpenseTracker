from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True

class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int
    date: datetime
    owner_id: int
    
    class Config:
        from_attributes = True
