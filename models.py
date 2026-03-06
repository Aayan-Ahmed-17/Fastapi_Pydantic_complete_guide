from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str
    fullname: Optional[str] = None
    birth_date: Optional[date] = None
    is_subscribed: bool = False