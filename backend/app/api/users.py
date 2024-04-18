from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from ..crud import users as crud
from ..schemas import users as schemas
from ..database import SessionLocal

router = APIRouter()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to fetch all users
@router.get("/users/", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# Route to fetch a single user by ID
@router.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Route to create a new user
@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if not crud.validate_email(user.email):
        raise HTTPException(status_code=400, detail="Invalid email address")

    # Проверяем, существует ли пользователь с таким адресом электронной почты
    existing_user = crud.get_user_by_email(db, user.email)
    print(existing_user)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Создаем нового пользователя
    return crud.create_user(db, user)

# Route to update an existing user
@router.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user)

# Route to delete a user
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)
