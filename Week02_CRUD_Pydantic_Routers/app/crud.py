posts_db = [
    {"id":1,"title":"First Post","content":"Hallo"},
    {"id":2,"title":"Second Post","content":"Hola"}
]

def get_all_posts():
    return posts_db

def get_post_by_id(post_id:int):
    for post in posts_db:
        if post["id"] == post_id:
            return post
        
    return None

def create_post(title: str, content: str):
    if posts_db:
        new_id = posts_db[-1]["id"] + 1

    new_post = {
        "id": new_post,
        "title": title,
        "content": content
    }

    posts_db.append(new_post)
    return new_post