from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.crud import create_post, get_posts, get_post_by_user, delete_post
from app.database import get_session
from app.models import Post

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/")
def create_post_endpoint(
    post: Post,
    session: Session = Depends(get_session)
):
    return create_post(session, post)

@router.get("/")
def get_posts_endpoint(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    user_id: int = Query(None),
    session: Session = Depends(get_session)
):
    return get_posts(
        session,
        page=page,
        limit=limit,
        user_id=user_id
    )

@router.get("/user/{user_id}")
def get_posts_by_user_endpoint(
    user_id: int,
    session: Session = Depends(get_session)
):
    return get_post_by_user(session, user_id)


@router.delete("/{post_id}")
def delete_post_endpoint(
    post_id: int,
    session: Session = Depends(get_session)
):
    post = delete_post(session, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return {"detail": "Post deleted successfully"}