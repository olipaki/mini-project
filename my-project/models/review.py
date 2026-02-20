from sqlalchemy import String, Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .reservation import Reservation
    from .user import User
    from .study import Study


class Review(Base):
    __tablename__ = "reviews"

    Review_ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    평점: Mapped[int] = mapped_column(Integer, nullable=False)  # 예: 1~5점
    내용: Mapped[str] = mapped_column(Text, nullable=True)

    # FK 설정: 어떤 예약에 대한 리뷰인지, 누가 썼는지, 어떤 스터디에 대한 것인지
    reservation_id: Mapped[int] = mapped_column(
        ForeignKey("reservations.Reservation_ID"), unique=True, nullable=False
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_ID"), nullable=False)
    study_id: Mapped[int] = mapped_column(ForeignKey("studies.Study_ID"), nullable=True)

    # 객체 간 관계 설정
    reservation: Mapped["Reservation"] = relationship("Reservation")
    user: Mapped["User"] = relationship("User")
    study: Mapped["Study"] = relationship("Study", back_populates="reviews")
