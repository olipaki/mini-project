from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.reservation_schema import ReservationCreate, ReservationResponse
from services import reservation_service

router = APIRouter(prefix="/reservations", tags=["예약"])


@router.post("/", response_model=ReservationResponse)
def create_reservation(data: ReservationCreate, db: Session = Depends(get_db)):
    # 서비스 계층 호출
    return reservation_service.make_new_reservation(
        db, data.user_id, data.room_id, data.날짜
    )
