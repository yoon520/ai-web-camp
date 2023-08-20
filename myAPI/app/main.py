from fastapi import FastAPI, HTTPException, status, Depends, Body, Header
from datetime import datetime, timedelta
from typing import Annotated, List
from jose import jwt

from myLogging import mylogger

from sqlalchemy.orm import Session
from database import SessionLocal

from schemas import User, UserBase, UserCreate, UserUpdate, Token, Webtoon, Book
from crud import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from crud import verify_password, create_access_token, get_current_active_user, update_user, delete_user
from crud import get_webtoon_by_title, get_book_by_title
from crud import get_user_by_user_id, create_user


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

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
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="존재하지 않는 사용자")

    if user.user_id == db_user.user_id:
        if verify_password(user.password, db_user.hashed_password):
            token_obj = {"sub":db_user.user_id}
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(token_obj, access_token_expires)

    if access_token is not None:
        return {"access_token": access_token }
    else:
        return {"message": "비밀번호 오류"}
    
# 회원 정보 수정
@app.put("/users")
def modify_account(current_user: Annotated[str, Depends(get_current_active_user)], user: UserUpdate, db: Session = Depends(get_db)):
    db_user = update_user(db, current_user, user)
    return db_user

# 회원 탈퇴
@app.delete("/users")
def delete_account(current_user: Annotated[str, Depends(get_current_active_user)], db: Session = Depends(get_db)):
    user_id = current_user
    delete_user(db, user_id)
    return {"message": "탈퇴 완료"}

# 로그아웃
@app.post("/logout")
def login():
    return {"message": "로그아웃 성공"}

# 토큰 확인
# @app.get("/token/me")
# async def check_token(
#     current_user: Annotated[str, Depends(get_current_active_user)]
# ):
#     return current_user

# 메인 페이지(게시글 가져오기)
@app.get("/board")
def get_posts(current_user: Annotated[str, Depends(get_current_active_user)], db: Session = Depends(get_db)):
    db_user = get_user_by_user_id(db, current_user)
    return

# 웹툰 찾기
@app.get("/webtoons/{w_title}", response_model=List[Webtoon])
def get_webtoon(w_title: str, db: Session = Depends(get_db)):
    db_webtoon = get_webtoon_by_title(db, w_title)
    return db_webtoon

# 책 찾기
@app.get("/books/{b_title}", response_model=List[Book])
def get_book(b_title: str,  db: Session = Depends(get_db)):
    db_book = get_book_by_title(db, b_title)
    return db_book

# 글 쓰기
@app.post("/board")
def wrtie_post(board: Board):
    mylogger.debug(board)
    return { "post_id": board.postId }

# 글 수정
@app.put("/board/{post_id}")
def modify_post(post_id: int, board: Board):
    mylogger.debug(Board)
    return { "post_id": board.postId }

# 글 삭제
@app.delete("/board/{post_id}")
def modify_post(post_id: int):
    return { "message": "삭제 성공" }

'''
# 해시태그 검색
@app.get("/hashtags/{hashtag}")
def search_hashtag(hashtag: str):
    return _sample_board
'''