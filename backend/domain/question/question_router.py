from venv import create
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

# from database import SessionLocal
from database import get_db
from domain.question import question_schema, question_crud
# from models import Question

router = APIRouter(
    prefix='/api/question',
)


"""
@router.get('/list')
def question_list():
    db = SessionLocal()
    _question_list = db.query(Question).order_by(
        Question.create_date.desc()).all()  # db 세션 생성 및 질문 목록 조회
    db.close()  # 사용한 db 세션을 컨넥션 풀에 반환 (세션 종료가 아님)
    return _question_list
"""

""" 2-1 번째 방법
@router.get('/list')
def question_list():
    with get_db() as db:
        _question_list = db.query(Question).order_by(
            Question.create_date.desc()).all()
    return _question_list
# 오류 여부에 상관없이 with 문을 벗어나는 순간 db.close()가 실행된다.
"""

# 2-2 방법


@router.get('/list', response_model=question_schema.QuestionList)
def question_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _question_list = question_crud.get_question_list(
        db, skip=page*size, limit=size
    )
    return {
        'total': total,
        'question_list': _question_list
    }


"""
get_db 함수를 with문과 함께 쓰는 대신 question_list 함수의 매개변수로 
db: Session = Depends(get_db) 객체를 주입받았다.
db: Session 문장의 의미는 db 객체가 Session 타입임을 의미한다.

FastAPI의 Depends는 매개 변수로 전달 받은 함수를 실행시킨 결과를 리턴한다.

response_model=list[question_schema.Question] 는 해당 함수의 리턴값이
Question 스키마로 구성된 리스트임을 의미한다.
"""


@router.get('/detail/{question_id}', response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question


@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)
