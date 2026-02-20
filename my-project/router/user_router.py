from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas.user import UserCreate, UserResponse
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # 서비스 계층 호출
    service = UserService(db)
    return service.register_user(user_data)
