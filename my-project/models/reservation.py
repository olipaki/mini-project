from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .room import Room


class Reservation(Base):
    __tablename__ = "reservations"

    Reservation_ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    날짜: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    회원: Mapped[str] = mapped_column(String(50))

    # ERD의 FK 반영: user_ID와 Room_ID 참조
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_ID"), nullable=False)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.Room_ID"), nullable=False)

    # 객체 간 관계 설정
    user: Mapped["User"] = relationship("User", back_populates="reservations")
    room: Mapped["Room"] = relationship("Room", back_populates="reservations")

