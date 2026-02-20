from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Reservation
from schemas.reservation import ReservationResponse
from typing import List

router = APIRouter(prefix="/reservations", tags=["예약"])


@router.get("/", response_model=List[ReservationResponse])
def get_all_reservations(db: Session = Depends(get_db)):
    # 화면에 필요한 예약 데이터를 모두 가져옵니다.
    return db.query(Reservation).all()
