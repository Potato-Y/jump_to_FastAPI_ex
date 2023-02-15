# import contextlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./backend.db'  # db 접속 주소, 프로젝트 루트 디렉터리에 저장

engine = create_engine(  # 컨넥션 풀을 생성한다.
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        'check_same_thread': False,
    },
)
# 컨넥션 풀이란, DB에 접속하는 객체를 일정 갯수만큼 만들어 놓고 돌려가며 사용하는 것
# 컨넥션 풀은 DB에 접속하는 세션수를 제어하고, 세션 접속에 소용되는 시간을 줄이고자 하는 용도로 사용

SessionLocal = sessionmaker(
    # commit 을 실행해야만 저장이 된다. / 데이터를 잘 못 저장했을 때 rolback으로 돌릴 수 있다.
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


# @contextlib.contextmanager
def get_db():  # db 세션 객체를 리턴하는 제너레이터 함수
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""ex
with get_db() as db:

with 문을 벗어나는 순간 get_db gkatndml finally에 작성한 db.close() 함수가
자동으로 실행된다.
"""
