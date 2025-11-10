from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.client import Client
from app.models.sale import Sale
from app.models.tractor import Tractor
from app.models.user import User
from app.schemas import SaleCreate, SaleResponse, SaleUpdate
from app.utils.auth import get_current_active_user

router = APIRouter(prefix="/sales", tags=["sales"])


def _validate_relations(
    db: Session, client_id: int, tractor_id: int, employee_id: int
) -> None:
    if not db.query(Client.id).filter(Client.id == client_id).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Client does not exist")
    if not db.query(Tractor.id).filter(Tractor.id == tractor_id).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tractor does not exist")
    if not db.query(User.id).filter(User.id == employee_id).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Employee does not exist")


@router.get("/", response_model=List[SaleResponse])
def list_sales(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)
) -> List[SaleResponse]:
    query = db.query(Sale)
    if current_user.role != "admin":
        query = query.filter(Sale.employee_id == current_user.id)
    return query.order_by(Sale.sale_date.desc()).all()


@router.post("/", response_model=SaleResponse, status_code=status.HTTP_201_CREATED)
def create_sale(
    sale_in: SaleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> SaleResponse:
    employee_id = sale_in.employee_id or current_user.id
    _validate_relations(db, sale_in.client_id, sale_in.tractor_id, employee_id)

    sale = Sale(
        client_id=sale_in.client_id,
        tractor_id=sale_in.tractor_id,
        employee_id=employee_id,
        sale_price=sale_in.sale_price,
        notes=sale_in.notes,
    )
    db.add(sale)
    db.commit()
    db.refresh(sale)
    return sale


@router.get("/{sale_id}", response_model=SaleResponse)
def get_sale(
    sale_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> SaleResponse:
    sale = db.query(Sale).filter(Sale.id == sale_id).first()
    if not sale:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale not found")
    if current_user.role != "admin" and sale.employee_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
    return sale


@router.put("/{sale_id}", response_model=SaleResponse)
def update_sale(
    sale_id: int,
    sale_in: SaleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> SaleResponse:
    sale = db.query(Sale).filter(Sale.id == sale_id).first()
    if not sale:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale not found")
    if current_user.role != "admin" and sale.employee_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")

    data = sale_in.dict(exclude_unset=True)

    if any(field in data for field in ("client_id", "tractor_id", "employee_id")):
        _validate_relations(
            db,
            data.get("client_id", sale.client_id),
            data.get("tractor_id", sale.tractor_id),
            data.get("employee_id", sale.employee_id),
        )

    for field, value in data.items():
        setattr(sale, field, value)

    db.commit()
    db.refresh(sale)
    return sale


@router.delete("/{sale_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sale(
    sale_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> None:
    sale = db.query(Sale).filter(Sale.id == sale_id).first()
    if not sale:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale not found")
    if current_user.role != "admin" and sale.employee_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
    db.delete(sale)
    db.commit()
