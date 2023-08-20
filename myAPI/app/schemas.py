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

class UserUpdate(BaseModel):
    password: str
    name: str
    profile: str = None
    phone: str

class User(UserBase):
    id: str
    name: str
    profile: str = None
    phone: str
    birth: date
    create_time: datetime

# 게시글
class BoardBase(BaseModel):
    title: str
    category: str
    author: str
    poster: str
    star: int
    content: str

class Board(BaseModel):
    boardId: int
    wrtieTime: datetime = None

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