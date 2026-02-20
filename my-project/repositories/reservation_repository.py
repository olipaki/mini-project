# # repositories/reservation_repo.py
# from sqlalchemy.orm import Session
# from models import Reservation
# from datetime import datetime


# # 1. 예약 데이터 저장 (CREATE)
# def create_reservation(db: Session, reservation_data: Reservation):
#     db.add(reservation_data)
#     db.commit()
#     db.refresh(reservation_data)
#     return reservation_data


# # 2. 특정 방의 특정 시간대 예약 조회 (READ - 중복 체크용)
# def get_reservation_by_time(db: Session, room_id: int, target_time: datetime):
#     return (
#         db.query(Reservation)
#         .filter(Reservation.room_id == room_id, Reservation.날짜 == target_time)
#         .first()
#     )


# # 3. 전체 예약 조회 (READ - 화면용)
# def get_all_reservations(db: Session):
#     return db.query(Reservation).all()
#####################################################

from sqlalchemy.orm import Session
from models.reservation import Reservation
from datetime import datetime


def save_reservation(db: Session, reservation: Reservation):
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation


def find_overlap(db: Session, room_id: int, target_time: datetime):
    # 같은 방, 같은 시간에 예약이 있는지 조회
    return (
        db.query(Reservation)
        .filter(Reservation.room_id == room_id, Reservation.날짜 == target_time)
        .first()
    )
