from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated
from ..database import SessionLocal
from ..crud import authentication as crud_auth
from ..crud import users as crud_users
from ..schemas import authentication as schemas_auth

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to fetch all activities
@router.post("/login")
async def create_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(SessionLocal)):
    print("STARTED")
    user = crud_auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = crud_auth.create_access_token(
        data={"sub": user.username}
    )
    return schemas_auth.Token(access_token=access_token, token_type="bearer")

def get_token(user_id: str, token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    key = crud_auth.get_key(db, user_id)
    if token != key:
        raise credentials_exception
    return crud_users.get_user(db, user_id)

def authenticate_user(db: Session, token: str):
    try:
        payload = oauth2_scheme.verify_token(token)
        username = payload.get("sub")
        if username is None:
            return None

        # user = db.query(User).filter(User.username == username).first()
        return crud_users.get_user_by_email(username)
    except Exception as e:
        print(f"Error authenticating user: {e}")
        return None