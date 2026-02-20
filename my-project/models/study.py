from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .review import Review  # 스터디에 대한 리뷰가 있다면 참조


class Study(Base):
    __tablename__ = "studies"

    Study_ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    스터디명: Mapped[str] = mapped_column(String(100), nullable=False)
    주제: Mapped[str] = mapped_column(String(50), nullable=True)
    설명: Mapped[str] = mapped_column(Text, nullable=True)

    # 스터디와 리뷰의 관계 (1:N)
    # 리뷰가 스터디룸이 아닌 '스터디' 자체에 달리는 경우를 가정했습니다.
    reviews: Mapped[List["Review"]] = relationship("Review", back_populates="study")
