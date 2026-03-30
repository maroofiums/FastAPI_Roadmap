from app.crud import create_post, get_posts, get_post_by_user, delete_post
from app.database import get_session
from app.models import Post
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=Post)
def create_post_endpoint(post: Post, session=Depends(get_session)):
    return create_post(session, post)

@router.get("/", response_model=list[Post])
def get_posts_endpoint(session=Depends(get_session)):
    return get_posts(session)

@router.get("/user/{user_id}", response_model=list[Post])
def get_posts_by_user_endpoint(user_id: int, session=Depends(get_session)):
    return get_post_by_user(session, user_id)

@router.delete("/{post_id}")
def delete_post_endpoint(post_id: int, session=Depends(get_session)):
    post = delete_post(session, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted successfully"}

