from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str

    posts: List["Post"] = Relationship(back_populates="user")

class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    user: Optional[User] = Relationship(back_populates="posts")
