# 🚀 Week 2 — Day by Day Plan (FastAPI)

## 📁 Your Structure

```
app/
 ├── routers/
 │    └── posts.py
 ├── __init__.py
 ├── crud.py
 ├── models.py
 └── schemas.py
main.py
README.md
```

---

# 📅 Day 1 — Project Setup + Basic Structure

## 🎯 Goal

* Setup folders
* Connect router to main app

## ✅ Tasks

* Create folder structure
* Create `main.py`
* Create empty router

## 🧠 Code

### main.py

```python
from fastapi import FastAPI
from app.routers import posts

app = FastAPI()

app.include_router(posts.router)

@app.get("/")
def root():
    return {"message": "API is running"}
```

### routers/posts.py

```python
from fastapi import APIRouter

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/")
def test():
    return {"message": "Posts route working"}
```

---

## 🧪 Test

Run:

```
uvicorn main:app --reload
```

Check:

* `/`
* `/posts`

---

# 📅 Day 2 — Models + Fake Database

## 🎯 Goal

* Understand data storage
* Create in-memory DB

## 📁 models.py

```python
posts_db = [
    {"id": 1, "title": "First Post", "content": "Hello"}
]
```

---

## 📁 crud.py (Read operations)

```python
from app.models import posts_db

def get_posts():
    return posts_db

def get_post(post_id: int):
    for post in posts_db:
        if post["id"] == post_id:
            return post
    return None
```

---

## 📁 routers/posts.py

```python
from app.crud import get_posts, get_post

@router.get("/")
def read_posts():
    return get_posts()

@router.get("/{post_id}")
def read_post(post_id: int):
    return get_post(post_id)
```

---

## 🧪 Task

* Add 2 more posts manually
* Test GET endpoints

---

# 📅 Day 3 — Schemas (Validation Layer)

## 🎯 Goal

* Learn Pydantic validation
* Separate request/response

## 📁 schemas.py

```python
from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
```

---

## 📁 routers/posts.py (update)

```python
from app.schemas import PostResponse

@router.get("/", response_model=list[PostResponse])
def read_posts():
    return get_posts()
```

---

## 🧪 Task

* Try sending wrong data → see validation error

---

# 📅 Day 4 — CREATE (POST)

## 🎯 Goal

* Add new data

## 📁 crud.py

```python
def create_post(data):
    new_post = {
        "id": len(posts_db) + 1,
        "title": data.title,
        "content": data.content
    }
    posts_db.append(new_post)
    return new_post
```

---

## 📁 routers/posts.py

```python
from app.schemas import PostCreate
from app.crud import create_post

@router.post("/", response_model=PostResponse)
def add_post(data: PostCreate):
    return create_post(data)
```

---

## 🧪 Task

* Use Swagger `/docs`
* Create 3 posts

---

# 📅 Day 5 — UPDATE (PUT) + Optional Fields

## 🎯 Goal

* Partial update
* Learn Optional

## 📁 schemas.py

```python
from typing import Optional

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
```

---

## 📁 crud.py

```python
def update_post(post_id: int, data):
    for post in posts_db:
        if post["id"] == post_id:
            if data.title:
                post["title"] = data.title
            if data.content:
                post["content"] = data.content
            return post
    return None
```

---

## 📁 routers/posts.py

```python
from app.schemas import PostUpdate
from fastapi import HTTPException

@router.put("/{post_id}", response_model=PostResponse)
def update(post_id: int, data: PostUpdate):
    post = update_post(post_id, data)
    if not post:
        raise HTTPException(status_code=404, detail="Not found")
    return post
```

---

## 🧪 Task

* Update only title
* Update only content

---

# 📅 Day 6 — DELETE + Error Handling

## 🎯 Goal

* Remove data
* Handle errors properly

## 📁 crud.py

```python
def delete_post(post_id: int):
    for i, post in enumerate(posts_db):
        if post["id"] == post_id:
            return posts_db.pop(i)
    return None
```

---

## 📁 routers/posts.py

```python
@router.delete("/{post_id}")
def delete(post_id: int):
    post = delete_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": "Deleted successfully"}
```

---

## 🧪 Task

* Delete a post
* Try deleting non-existing → check error

---

# 📅 Day 7 — Final Polish + Features

## 🎯 Goal

* Make API more real-world

## 🔥 Add Features

### 1. Query Search

```python
@router.get("/")
def read_posts(title: str = None):
    if title:
        return [p for p in posts_db if title.lower() in p["title"].lower()]
    return posts_db
```

---

### 2. Pagination

```python
def read_posts(skip: int = 0, limit: int = 5):
    return posts_db[skip: skip + limit]
```

---

### 3. Add created_at

```python
from datetime import datetime

"created_at": datetime.now()
```


---

# 🧠 End of Week 2 — You Can Now

* Build structured backend
* Write clean APIs
* Handle CRUD
* Use routers
* Validate data

---

