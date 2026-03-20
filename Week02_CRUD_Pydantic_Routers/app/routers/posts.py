from fastapi import APIRouter

router = APIRouter(prefix="/posts",tags=["Posts"])

@router.get("/")
def test():
    return {"message":"Posts Routes Running..."}
