from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select

from app.database import get_session
from app.models import User
from app.schemas import UserCreate, UserRead
from app.crud import create_user
from app.core.security import verify_password, create_access_token


router = APIRouter()


@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_session)):
    db_user = create_user(
        db=db,
        username=user.username,
        email=user.email,
        password=user.password
    )

    return UserRead.model_validate(db_user)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_session)
):
    statement = select(User).where(User.username == form_data.username)
    user = db.exec(statement).first()

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    token = create_access_token(data={"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }