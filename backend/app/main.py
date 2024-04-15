from fastapi import FastAPI
from .api import activities, users

app = FastAPI()

# Подключаем роуты для активностей и пользователей
app.include_router(activities.router)
app.include_router(users.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
