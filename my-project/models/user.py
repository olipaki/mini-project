from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .reservation import Reservation


class User(Base):
    __tablename__ = "users"

    user_ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    이름: Mapped[str] = mapped_column(String(50), nullable=False)
    전화번호: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    주소: Mapped[Optional[str]] = mapped_column(String(200))

    # 1:N 관계 (한 명의 유저는 여러 예약을 가짐)
    reservations: Mapped[List["Reservation"]] = relationship(
        "Reservation", back_populates="user"
    )
