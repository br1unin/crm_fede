from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SaleBase(BaseModel):
    client_id: int
    tractor_id: int
    employee_id: Optional[int] = None
    sale_price: float
    notes: Optional[str] = None


class SaleCreate(SaleBase):
    pass


class SaleUpdate(BaseModel):
    client_id: Optional[int] = None
    tractor_id: Optional[int] = None
    employee_id: Optional[int] = None
    sale_price: Optional[float] = None
    notes: Optional[str] = None


class SaleResponse(SaleBase):
    id: int
    sale_date: datetime

    class Config:
        orm_mode = True
