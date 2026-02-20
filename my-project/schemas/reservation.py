from pydantic import BaseModel
from datetime import datetime


class ReservationBase(BaseModel):
    user_id: int
    room_id: int
    날짜: datetime


class ReservationCreate(ReservationBase):
    pass  # 생성 시 검증용


class ReservationResponse(ReservationBase):
    Reservation_ID: int

    class Config:
        from_attributes = True  # ORM 모델을 자동으로 읽어옴
