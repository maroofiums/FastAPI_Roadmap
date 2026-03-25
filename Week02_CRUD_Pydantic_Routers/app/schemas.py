from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None