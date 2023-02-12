from fastapi import APIRouter

from database import SessionLocal
from models import Question

router = APIRouter(
    prefix='/api/question',
)


@router.get('/list')
def question_list():
    db = SessionLocal()
    _question_list = db.query(Question).order_by(
        Question.create_date.desc()).all()  # db 세션 생성 및 질문 목록 조회
    db.close()  # 사용한 db 세션을 컨넥션 풀에 반환 (세션 종료가 아님)
    return _question_list
