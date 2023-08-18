from pydantic import BaseModel
from datetime import datetime, date

# 토큰
class Token(BaseModel):
    access_token: str

# 회원
class UserBase(BaseModel):
    user_id: str
    password: str

class UserCreate(UserBase):
    name: str
    profile: str = None
    phone: str
    birth: date

class User(UserBase):
    id: str
    create_time: datetime

    class Config:
        orm_mode = True

# 게시글
class Board(BaseModel):
    boardId: int
    userId: int
    title: str
    category: str
    author: str
    poster: str
    star: int
    content: str
    wrtieTime: datetime = None
    hashtag: list[str] = []

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