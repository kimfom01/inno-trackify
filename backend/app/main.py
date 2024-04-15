from fastapi import FastAPI
from .api import activities, users
from .database import create_tables

app = FastAPI()

# Создаем таблицы в базе данных
create_tables()

# Подключаем роуты для активностей, пользователей и событий
app.include_router(activities.router)
app.include_router(users.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
