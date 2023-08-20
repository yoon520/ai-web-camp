## Basic modules
from typing import Annotated, Union
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status

## jwt & oauth2
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

## custom modules & db
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
import models, schemas

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

## Utils functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt   

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return user_id

async def get_current_active_user(
    current_user: Annotated[str, Depends(get_current_user)]
):
    if not current_user:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

## object CRUD
def get_user(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()

def get_user_by_user_id(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        user_id=user.user_id, 
        hashed_password=hashed_password,
        name=user.name,
        profile=user.profile,
        birth=user.birth,
        phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: str, user:schemas.UserUpdate):
    hashed_password = get_password_hash(user.password)
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    db_user.hashed_password = hashed_password
    db_user.name = user.name
    db_user.profile = user.profile
    db_user.phone = user.phone
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: str):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user

def get_webtoon_by_title(db: Session, title: str):
    try:
        return db.query(models.Webtoon).filter(models.Webtoon.title == title).all()
    except NoResultFound:
        return "데이터 없음"

def get_book_by_title(db: Session, title: str):
    try:
        return db.query(models.Book).filter(models.Book.title == title).all()
    except NoResultFound:
        return "데이터 없음"

def get_board_all_by_id(db: Session, id: int):
    db_user = db.query(models).filter(models.Board).filter(models.User.owner)