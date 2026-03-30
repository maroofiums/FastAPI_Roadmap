from sqlmodel import Session, select
from app.models import User, Post

def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_users(session: Session, user_id: int):
    return session.exec(select(User)).all()

def get_user(session: Session, user_id: int):
    return session.get(User, user_id)

def delete_user(session: Session, user_id: int):
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False

def create_post(session: Session, post: Post):
    session.add(post)
    session.commit()
    session.refresh(post)
    return post

def get_posts(session: Session):
    return session.exec(select(Post)).all()

def get_post_by_user(session: Session, user_id: int):
    return session.exec(select(Post).where(Post.user_id == user_id)).all()

def delete_post(session: Session, post_id: int):
    post = session.get(Post, post_id)
    if post:
        session.delete(post)
        session.commit()
        return True
    return False

