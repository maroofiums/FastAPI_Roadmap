from pydantic import BaseModel

# Models

class ItemCreate(BaseModel):
    name: str
    price: float
    description: str 
    in_stock: bool

class ItemResponse(BaseModel):
    name: str
    price: float