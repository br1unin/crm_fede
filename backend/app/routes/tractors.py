from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.tractor import Tractor
from app.models.user import User
from app.schemas import TractorCreate, TractorResponse, TractorUpdate
from app.utils.auth import get_current_active_user, require_admin

router = APIRouter(prefix="/tractors", tags=["tractors"])


@router.get("/", response_model=List[TractorResponse])
def list_tractors(
    db: Session = Depends(get_db), _: User = Depends(get_current_active_user)
) -> List[TractorResponse]:
    return db.query(Tractor).order_by(Tractor.id.desc()).all()


@router.post("/", response_model=TractorResponse, status_code=status.HTTP_201_CREATED)
def create_tractor(
    tractor_in: TractorCreate,
    db: Session = Depends(get_db),
    _: User = Depends(require_admin),
) -> TractorResponse:
    tractor = Tractor(**tractor_in.dict())
    db.add(tractor)
    db.commit()
    db.refresh(tractor)
    return tractor


@router.get("/{tractor_id}", response_model=TractorResponse)
def get_tractor(
    tractor_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_active_user),
) -> TractorResponse:
    tractor = db.query(Tractor).filter(Tractor.id == tractor_id).first()
    if not tractor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tractor not found")
    return tractor


@router.put("/{tractor_id}", response_model=TractorResponse)
def update_tractor(
    tractor_id: int,
    tractor_in: TractorUpdate,
    db: Session = Depends(get_db),
    _: User = Depends(require_admin),
) -> TractorResponse:
    tractor = db.query(Tractor).filter(Tractor.id == tractor_id).first()
    if not tractor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tractor not found")
    for field, value in tractor_in.dict(exclude_unset=True).items():
        setattr(tractor, field, value)
    db.commit()
    db.refresh(tractor)
    return tractor


@router.delete("/{tractor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tractor(
    tractor_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(require_admin),
) -> None:
    tractor = db.query(Tractor).filter(Tractor.id == tractor_id).first()
    if not tractor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tractor not found")
    db.delete(tractor)
    db.commit()
