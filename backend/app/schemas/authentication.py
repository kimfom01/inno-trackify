import datetime
from pydantic import BaseModel

# Схема для входных данных пользователя
class AuthenticationKeysBase(BaseModel):
    user_id: int
    key: str
    due_date: str

# Схема для создания пользователя
class AuthenticationKeysCreate(AuthenticationKeysBase):
    pass

# Схема для обновления пользователя
class AuthenticationKeysUpdate(AuthenticationKeysBase):
    pass

# Схема для возвращаемых данных пользователя
class AuthenticationKeys(AuthenticationKeysBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
