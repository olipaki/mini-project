from pydantic import BaseModel, EmailStr
from typing import Optional


# 유저 생성을 위해 클라이언트가 보내는 데이터 양식
class UserCreate(BaseModel):
    이름: str
    전화번호: str
    email: EmailStr
    주소: Optional[str] = None


# 서버가 유저 정보를 응답할 때 보내는 데이터 양식
class UserResponse(BaseModel):
    user_ID: int
    이름: str
    email: EmailStr

    class Config:
        from_attributes = True  # SQLAlchemy 모델 데이터를 자동으로 변환해줌
