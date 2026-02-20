from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from schemas.user import UserCreate
from fastapi import HTTPException


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register_user(self, user_data: UserCreate):
        # [비즈니스 로직] 이메일 중복 체크
        existing_user = self.repository.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="이미 등록된 이메일입니다.")

        return self.repository.create(user_data)
