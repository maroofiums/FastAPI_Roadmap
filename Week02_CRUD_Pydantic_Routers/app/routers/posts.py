from fastapi import APIRouter,HTTPException
from app.crud import get_all_posts,update_post,get_post_by_id,create_post
from app.schemas import PostCreate,PostResponse,PostUpdate

router = APIRouter(prefix="/posts",tags=["Posts"])

@router.get("/test")
def test():
    return {"message":"Posts Routes Running..."}

@router.get("/")
def get_all():
    return get_all_posts()

@router.get("/{post_id}")
def get_id(post_id: int):
    post = get_post_by_id(post_id)

    if not post:
        raise HTTPException(status_code=404,detail="Post not found")
    
    return post

@router.post("/",response_model=PostResponse) 
def create(data: PostCreate): 
    return create_post(data) 

@router.put("/{post_id}",response_model= PostUpdate)
def update(post_id: int, data: PostUpdate):
    post = update_post(post_id,data)
    if not post:
        raise HTTPException(status_code = 404,detail = "Not Found")
    return post
