from fastapi import FastAPI
from database import engine, Base
import models
from router import reservation  # 라우터 파일이 있다면 연결

# DB 테이블 생성 (이미 생성된 모델들을 기반으로)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Study Room API")

# 라우터 등록
# app.include_router(reservation.router)


@app.get("/")
def root():
    return {"message": "스터디룸 예약 시스템이 가동 중입니다."}


