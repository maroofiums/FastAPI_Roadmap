from sqlmodel import Session
from app.models import User
from app.core.security import get_hashed_password

def create_user(db: Session, username: str,email:str, password: str) -> User:
    hashed_password = get_hashed_password(password)
    user = User(
        username=username, 
        email=email,
        hashed_password=hashed_password
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user