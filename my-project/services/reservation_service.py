from sqlalchemy.orm import Session
from fastapi import HTTPException
from repository import reservation_repo
from models.reservation import Reservation
from datetime import datetime


def make_new_reservation(db: Session, user_id: int, room_id: int, date: datetime):
    # 1. 비즈니스 로직: 운영시간 체크 (9-18시)
    if not (9 <= date.hour < 18):
        raise HTTPException(
            status_code=400, detail="운영 시간(09:00~18:00)이 아닙니다."
        )

    # 2. Repository 호출: 중복 예약 확인
    exists = reservation_repo.find_overlap(db, room_id, date)
    if exists:
        raise HTTPException(status_code=400, detail="이미 예약된 시간대입니다.")

    # 3. 객체 생성 및 저장 요청
    new_res = Reservation(user_id=user_id, room_id=room_id, 날짜=date, 회원="일반")
    return reservation_repo.save_reservation(db, new_res)
