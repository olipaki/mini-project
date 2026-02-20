from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_data: UserCreate) -> User:
        # Pydantic 모델을 DB 모델로 변환하여 저장
        db_user = User(**user_data.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()
