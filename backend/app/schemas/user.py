from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, EmailStr, constr


class UserBase(BaseModel):
    email: EmailStr
    name: constr(strip_whitespace=True, min_length=1, max_length=100)
    role: Literal["admin", "employee"] = "employee"
    is_active: bool = True


class UserCreate(UserBase):
    password: constr(min_length=6, max_length=128)


class UserUpdate(BaseModel):
    name: Optional[constr(strip_whitespace=True, min_length=1, max_length=100)] = None
    role: Optional[Literal["admin", "employee"]] = None
    is_active: Optional[bool] = None
    password: Optional[constr(min_length=6, max_length=128)] = None


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
