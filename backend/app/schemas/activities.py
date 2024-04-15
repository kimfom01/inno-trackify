from pydantic import BaseModel

# Схема для входных данных активностей
class ActivityBase(BaseModel):
    name: str

# Схема для создания активностей
class ActivityCreate(ActivityBase):
    pass

# Схема для обновления активностей
class ActivityUpdate(ActivityBase):
    pass

# Схема для возвращаемых данных активностей
class Activity(ActivityBase):
    id: int

    class Config:
        orm_mode = True