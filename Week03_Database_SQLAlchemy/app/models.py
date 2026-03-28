from app.database import Base
from sqlalchemy import Column,String,Integer,ForeignKey

class User(Base):
    __tabelname__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    user_id = Column(Integer,ForeignKey("users.id"))
