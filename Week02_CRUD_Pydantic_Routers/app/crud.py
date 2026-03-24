from app.models import posts_db
from app.schemas import PostCreate, PostUpdate

def get_all_posts():
    return posts_db

def get_post_by_id(post_id:int):
    for post in posts_db:
        if post["id"] == post_id:
            return post
        
    return None

def create_post(data: PostCreate):
    if posts_db:
        new_id = posts_db[-1]["id"] + 1
    else:
        new_id = 1

    new_post = {
        "id": new_id,
        "title": data.title,
        "content": data.content
    }

    posts_db.append(new_post)

    return new_post

def update_post(post_id:int,data:PostUpdate):
    for post in posts_db:
        if post["id"] == post_id:
            if data.title:
                post["title"] = data.title
            if data.content:
                post["content"] = data.content
            return post
    return None

def delete_post(post_id: int):
    for i,post in enumerate(posts_db):
        if post_id == post["id"]:
            return posts_db.pop(i)
    return None

