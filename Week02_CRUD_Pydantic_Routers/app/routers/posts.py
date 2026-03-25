from fastapi import APIRouter, HTTPException
from app.crud import get_all_posts, update_post, get_post_by_id, create_post, delete_post
from app.schemas import PostCreate, PostResponse, PostUpdate
from typing import Optional, List

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/test")
def test():
    return {"message": "Posts Routes Running..."}

@router.get("/", response_model=List[PostResponse])
def get_all(
    title: Optional[str] = None,
    skip: int = 0,
    limit: int = 5,
):
    results = get_all_posts()  

    if title:
        results = [p for p in results if title.lower() in p["title"].lower()]

    results = results[skip: skip + limit]

    return results

@router.get("/{post_id}", response_model=PostResponse)
def get_id(post_id: int):
    post = get_post_by_id(post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post

@router.post("/", response_model=PostResponse)
def create(data: PostCreate):
    return create_post(data)

@router.put("/{post_id}", response_model=PostResponse)  
def update(post_id: int, data: PostUpdate):
    post = update_post(post_id, data)
    if not post:
        raise HTTPException(status_code=404, detail="Not Found")
    return post

@router.delete("/{post_id}")
def delete(post_id: int):
    post = delete_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Not Found")
    return {"message": "Deleted Successfully"}