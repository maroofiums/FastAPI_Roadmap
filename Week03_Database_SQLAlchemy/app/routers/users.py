from app.crud import create_user, get_users, get_user, delete_user
from app.database import get_session
from app.models import User
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
def create_user_endpoint(user: User, session=Depends(get_session)):
    return create_user(session, user)

@router.get("/", response_model=list[User])
def get_users_endpoint(session=Depends(get_session)):
    return get_users(session)

@router.get("/{user_id}", response_model=User)
def get_user_endpoint(user_id: int, session=Depends(get_session)):
    user = get_user(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user_endpoint(user_id: int, session=Depends(get_session)):
    success = delete_user(session, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}

