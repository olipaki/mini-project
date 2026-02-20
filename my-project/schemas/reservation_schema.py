from pydantic import BaseModel
from datetime import datetime


class ReservationCreate(BaseModel):
    user_id: int
    room_id: int
    날짜: datetime


class ReservationResponse(BaseModel):
    Reservation_ID: int
    user_id: int
    room_id: int
    날짜: datetime

    class Config:
        from_attributes = True
