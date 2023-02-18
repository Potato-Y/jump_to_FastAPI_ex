import datetime
from pydantic import BaseModel, validator


class AnswerCreate(BaseModel):
    content: str

    @validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    """
    not_empty 함수는 AnswerCreate 스키마에 content 값이 저장될 때 실행된다.
    content의 값이 빈 경우 오류가 발생한다.
    """


class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True
