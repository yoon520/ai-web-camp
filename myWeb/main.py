from fastapi import FastAPI
from datetime import date, datetime
from pydantic import BaseModel
from typing import Union
import logging
import sys

mylogger = logging.getLogger("mylogger")

formatter = logging.Formatter('[%(levelname)s] %(message)s')

handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

mylogger.addHandler(handler)
mylogger.setLevel(logging.DEBUG)

app = FastAPI()

_sample_users = [
    {"id": 1, "userId": "hong123", "password": "1234", "profile": "image.jpg", "name": "홍길동", "phone": "01012341234", "validation": True, "createTime": date.today()},
    {"id": 2, "userId": "kim123", "password": "1111", "profile": "image.jpg", "name": "김철수", "phone": "01011112222", "validation": True, "createTime": date.today()},
]
_sample_board = [
    {
        "postId": 1,
        "userId": 1,
	    "title": "화산귀환",
	    "category": "웹툰",
	    "author": "비가/리코",
        "poster": "cover.jpg",
	    "star": 5,
	    "content": "재미있다",
        "writeTime": "2023-08-16T15:53:00+05:00", 
        "hashtag": ["#무협", "#회귀", "#먼치킨"]
    },
    {
        "postId": 2,
        "userId": 1,
        "title": "전독시",
	    "category": "웹툰",
	    "author": "싱숑/UMI/슬리피-C",
        "poster": "cover.jpg",
	    "star": 5,
	    "content": "재미있다",
        "writeTime": "2023-08-16T15:53:00+05:00", 
        "hashtag": ["#무협", "#회귀", "#먼치킨"]
    }
]

# DTO
# 회원
class User(BaseModel):
    userId: str
    password: str = None
    profile: str = None
    name: str = None
    phone: str = None
    validation: bool = None
    writeTime: datetime = None

# 게시글
class Board(BaseModel):
    postId: int
    userId: int
    title: str
    category: str
    author: str
    poster: str
    star: int
    content: str
    wrtieTime: datetime = None
    hashtag: str = None

# 웹툰
class Webtoon(BaseModel):
    bookId: int
    title: str
    author: str
    cover: str

# 책
class Book(BaseModel):
    bookId: int
    title: str
    author: str
    cover: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 아이디 중복 체크
@app.post("/users")
def check_id(user: User):
    mylogger.debug(user)
    return { "message": "사용 가능한 아이디" }

# 회원가입
@app.post("/signup")
def sign_up(user: User):
    mylogger.debug(user)
    return {"message": "가입 완료"}

# 로그인
@app.post("/login")
def login(user: User):
    mylogger.debug(user)
    return {"message": "로그인 성공"}

# 로그아웃
@app.post("/logout")
def login():
    return {"message": "로그아웃 성공"}

# 회원 정보 수정
@app.put("/users/{id}")
def modify_account(id: int, user: User):
    mylogger.debug(user)
    return {"message": "수정 완료"}

# 회원 탈퇴
@app.delete("/users/{id}")
def delete_account(id: int):
    mylogger.debug(id)
    return {"message": "탈퇴 완료"}

# 메인 페이지(게시글 가져오기)
@app.get("/users/{id}/board")
def get_posts(id: int):
    return _sample_board

# 웹툰 찾기
@app.get("/webtoons/{w_title}")
def get_webtoon(w_title: str):
    return w_title

# 책 찾기
@app.get("/books/{b_title}")
def get_webtoon(b_title: str):
    return b_title

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

# 해시태그 검색
@app.get("/hashtags/{hashtag}")
def search_hashtag(hashtag: str):
    return _sample_board