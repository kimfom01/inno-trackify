import hashlib
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from .. import models
from ..schemas import authentication as schemas
from ..schemas import users as user_schemas
from datetime import datetime, timedelta
import hmac

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


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta or timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = hmac.new(msg=str(to_encode).encode(), digestmod=hashlib.sha256).hexdigest()
    return encoded_jwt