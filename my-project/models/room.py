from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .reservation import Reservation

class Room(Base):
    __tablename__ = "rooms"

    Room_ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    방이름: Mapped[str] = mapped_column(String(50), nullable=False)
    수용인원: Mapped[int] = mapped_column(Integer)

    reservations: Mapped[List["Reservation"]] = relationship("Reservation", back_populates="room")