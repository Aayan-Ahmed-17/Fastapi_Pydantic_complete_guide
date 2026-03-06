from pydantic import BaseModel, EmailStr # type: ignore
from typing import Optional
from datetime import date

class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str
    fullname: Optional[str] = None
    birth_date: Optional[date] = None
    is_subscribed: bool = False

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int = 1