from fastapi import APIRouter,Path,Query
from app.models import ItemResponse,ItemCreate
from typing import List
route = APIRouter()

items_db: List[ItemCreate] = []

@route.get("/")
def greet():
    return {"msg":"Hello"}

@route.get("/ping")
def pong():
    return {"msg":"pong"}

@route.get("/health")
def healthy():
    return {"msg":"healthy"}

@route.get("/items/",response_model = [ItemResponse])
def get_items():
    return items_db

@route.post("/items/",response_model = ItemResponse)
def create_items(item:ItemCreate):
    items_db.append(item)   
    return item

@route.get("/items/{item_id}",response_model = ItemResponse)
def get_item(item_id:int):
    return items_db[item_id]

@route.put("/items/{item_id}",response_model = ItemResponse)
def get_item(item_id:int,item:ItemCreate):
    items_db[item_id] = item
    return item

@route.delete("/items/{item_id}")
def get_item(item_id:int):
    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted", "item": deleted_item.name}