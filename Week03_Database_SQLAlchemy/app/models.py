from app.database import Base
from sqlalchemy import Column,String,Integer,ForeignKey

class User(Base):
    __tabelname__ = "users"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    
    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True)
    title = Column(String)

    user_id = Column(Integer,ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")