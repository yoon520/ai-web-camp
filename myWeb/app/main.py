
from fastapi import FastAPI, HTTPException, Depends, Body, Header
from datetime import datetime, timedelta
from jose import jwt

from myLogging import mylogger

from sqlalchemy.orm import Session
from database import SessionLocal

from schemas import User, UserCreate, Token
from crud import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from crud import verify_password, create_access_token
from crud import get_user_by_user_id, create_user

from schemas import UserBase, UserCreate, Token


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

session_list = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 아이디 중복 체크
@app.get("/users/{user_id}")
def check_id(user_id: str, db: Session = Depends(get_db)):
    db_user = get_user_by_user_id(db, user_id=user_id)
    if db_user:
        raise HTTPException(status_code=400, detail="이미 사용하고 있는 아이디입니다.")
    return { "message":"사용 가능한 아이디입니다." }

# 회원가입
@app.post("/signup")
def sign_up(user: UserCreate, db: Session = Depends(get_db)):
    # insert new user_id
    create_user(db=db, user=user)
    return user

# 로그인
@app.post("/login")
def login(user: UserBase, db: Session = Depends(get_db)):
    # 로그인할 때
    # parameter: userid, password:
    # step1: userid 있는지 확인
    access_token = None
    db_user = get_user_by_user_id(db, user.user_id)

    if user.user_id == db_user.user_id:
        if verify_password(user.password, db_user.hashed_password):
            session_list.append({"num": len(session_list) , "loginId": db_user.user_id, "loginAt": datetime.now()})
            token_obj = {"sub":db_user.user_id}
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(token_obj, access_token_expires)
            mylogger.debug(session_list)

    if access_token is not None:
        return {"access_token": access_token}
    else:
        return {"message": "login falied"}

@app.post("/users")
async def get_user_token(token: Token):
    payload = jwt.decode(token.access_token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id: str = payload.get("sub")
    return {"user_id":user_id}

# # 로그아웃
# @app.post("/logout")
# def login():
#     return {"message": "로그아웃 성공"}

# # 회원 정보 수정
# @app.put("/users/{id}")
# def modify_account(id: int, user: User):
#     mylogger.debug(user)
#     return {"message": "수정 완료"}

# # 회원 탈퇴
# @app.delete("/users/{id}")
# def delete_account(id: int):
#     mylogger.debug(id)
#     return {"message": "탈퇴 완료"}

# # 메인 페이지(게시글 가져오기)
# @app.get("/users/{id}/board")
# def get_posts(id: int):
#     return _sample_board

# # 웹툰 찾기
# @app.get("/webtoons/{w_title}")
# def get_webtoon(w_title: str):
#     return w_title

# # 책 찾기
# @app.get("/books/{b_title}")
# def get_webtoon(b_title: str):
#     return b_title

# # 글 쓰기
# @app.post("/board")
# def wrtie_post(board: Board):
#     mylogger.debug(board)
#     return { "post_id": board.postId }

# # 글 수정
# @app.put("/board/{post_id}")
# def modify_post(post_id: int, board: Board):
#     mylogger.debug(Board)
#     return { "post_id": board.postId }

# # 글 삭제
# @app.delete("/board/{post_id}")
# def modify_post(post_id: int):
#     return { "message": "삭제 성공" }

# # 해시태그 검색
# @app.get("/hashtags/{hashtag}")
# def search_hashtag(hashtag: str):
#     return _sample_board