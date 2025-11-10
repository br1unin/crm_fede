from datetime import datetime
from typing import Optional

from pydantic import BaseModel, constr


class TractorBase(BaseModel):
    model: constr(strip_whitespace=True, min_length=1, max_length=100)
    brand: constr(strip_whitespace=True, min_length=1, max_length=50)
    year: Optional[int] = None
    price: Optional[float] = None
    status: constr(strip_whitespace=True, min_length=3, max_length=20) = "available"
    description: Optional[str] = None


class TractorCreate(TractorBase):
    pass


class TractorUpdate(BaseModel):
    model: Optional[constr(strip_whitespace=True, min_length=1, max_length=100)] = None
    brand: Optional[constr(strip_whitespace=True, min_length=1, max_length=50)] = None
    year: Optional[int] = None
    price: Optional[float] = None
    status: Optional[constr(strip_whitespace=True, min_length=3, max_length=20)] = None
    description: Optional[str] = None


class TractorResponse(TractorBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
