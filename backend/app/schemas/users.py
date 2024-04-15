from pydantic import BaseModel
from typing import Optional

# Схема для входных данных пользователя
class UserBase(BaseModel):
    email: str
    password: str
    username: str

# Схема для создания пользователя
class UserCreate(UserBase):
    pass

# Схема для обновления пользователя
class UserUpdate(UserBase):
    pass

# Схема для возвращаемых данных пользователя
class User(UserBase):
    id: int

    class Config:
        orm_mode = True
