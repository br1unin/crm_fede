from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, constr


class ClientBase(BaseModel):
    name: constr(strip_whitespace=True, min_length=1, max_length=100)
    company: Optional[constr(strip_whitespace=True, max_length=100)] = None
    phone: Optional[constr(strip_whitespace=True, max_length=20)] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    client_type: constr(strip_whitespace=True, min_length=3, max_length=20) = "potential"
    notes: Optional[str] = None
    employee_id: Optional[int] = None


class ClientCreate(ClientBase):
    name: constr(strip_whitespace=True, min_length=1, max_length=100)


class ClientUpdate(BaseModel):
    name: Optional[constr(strip_whitespace=True, min_length=1, max_length=100)] = None
    company: Optional[constr(strip_whitespace=True, max_length=100)] = None
    phone: Optional[constr(strip_whitespace=True, max_length=20)] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    client_type: Optional[constr(strip_whitespace=True, min_length=3, max_length=20)] = None
    notes: Optional[str] = None
    employee_id: Optional[int] = None


class ClientResponse(ClientBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
