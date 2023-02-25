from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Question(Base):
    __tablename__ = "question"  # __tablename__은 모델에 의해 관리되는 테이블의 이름을 뜻함

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)  # 제목
    content = Column(Text, nullable=False)  # 내용
    create_date = Column(DateTime, nullable=False)  # 작성 일시
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship('User', backref='question_users')


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey('question.id'))
    # question.id는 question 테이블의 id 컬럼이다.
    # (참조한 모델명, backref=역참조 설정)
    question = relationship('Question', backref='answers')
    # relationship 으로 question 속성을 생성하면 답변 객체 (answer)에서 연결된 질문의 제목을 answer.question.subject 처럼 참조할 수 있다.
    # 역참조란 질문에서 답변을 거꾸로 참조하는 것을 의미. 한 질문에 여러 답반이 달리는데, 역참조는 이 질문에 달린 답변들을 참조할 수 있게 한다.
    # 어떤 질문에 대항하는 객체가 a_question이라면 a_question.answers와 같은 코드로 해당 질문에 달린 답변들을 참조할 수 있다.
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship('User', backref='answer_users')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
