from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime, CheckConstraint
from datetime import datetime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True)
    hashed_password = Column(String)
    profile = Column(String, default="profile.jpg")
    name = Column(String)
    birth = Column(Date)
    phone = Column(String)
    create_time = Column(DateTime, default= datetime.now())

    board = relationship("Board", back_populates="owner")

class Board(Base):
    __tablename__ = "board"

    board_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    title = Column(String)
    category = Column(String)
    author = Column(String)
    poster = Column(String, default="noImg_view.png")
    star = Column(Integer)
    content = Column(String)
    write_time = Column(DateTime)

    owner = relationship("User", back_populates="board")

class Webtoon(Base):
    __tablename__ = "webtoon"

    webtoon_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    cover = Column(String, default="noImg_view.png")
    service = Column(String)
    update_day = Column(String)

class Book(Base):
    __tablename__ = "book"

    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    description = Column(String)
    cover = Column(String, default="noImg_view.png")
    publisher = Column(String)
    publish_date = Column(Date)