from fastapi import APIRouter,Path,Query

route = APIRouter()

@route.get("/")
def greet():
    return {"msg":"Hello"}

@route.get("/ping")
def pong():
    return {"msg":"pong"}

@route.get("/health")
def healthy():
    return {"msg":"healthy"}

@route.get("/items/{item_id}")
def read_item(item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000)):
        return {"item_id": item_id}

@route.get("/search")
def search_items(q: str = Query(..., min_length=3, max_length=50, regex="^[a-zA-Z0-9]+$")):
    return {"q": q}

