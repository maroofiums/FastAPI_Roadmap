from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.crud import create_user
from app.schemas import UserCreate,UserRead

router = APIRouter()

@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_session)):
    
    db_user = create_user(
        db=db, 
        username=user.username, 
        email=user.email, 
        password=user.password
    )

    return db_user


