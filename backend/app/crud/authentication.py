import hashlib
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from .. import models
from ..schemas import authentication as schemas
from ..schemas import users as user_schemas
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

# Функция для получения ключа по идентификатору пользователя
def get_key(db: Session, user_id: int):
    return db.query(models.Authentication_Keys.KEY).filter(models.Authentication_Keys.USER_ID == user_id).first()

# Функция для создания нового ключа
def add_user_key(db: Session, auth_key: schemas.AuthenticationKeysCreate):
    db_key = models.Authentication_Keys(user_id = auth_key.user_id, key = auth_key.key, due_date = auth_key.due_date)
    db.add(db_key)
    db.commit()
    db.refresh(db_key)
    return db_key

def authenticate_user(db: Session, username: str, password: str):
    return db.query(models.User).filter(models.User.username == username, models.User.password == password).first()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def get_username_from_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
    return payload.get("sub") 
