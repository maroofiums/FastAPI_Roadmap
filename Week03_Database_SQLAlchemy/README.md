# 🚀 Week 3 — FULL 7 DAY ROADMAP (Database Integration)

---

# 📅 **Day 1 — Database Setup + Core Concepts**

## 🎯 Goal

Understand how backend connects to database

## 🧠 Learn (45–60 min)

* What is ORM
* Engine vs Session
* Why DB session lifecycle matters

👉 Tool:

* SQLAlchemy

---

## 🛠️ Build (1.5–2 hrs)

* Create `database.py`
* Setup SQLite DB
* Create:

  * `engine`
  * `SessionLocal`
  * `Base`
* Add `get_db()` dependency

---

## 🔥 Test Yourself

* What is `commit()` vs `refresh()`?
* Why do we close DB session?

---

## ✅ Outcome

✔ DB connected to FastAPI
✔ You understand session lifecycle

---

# 📅 **Day 2 — Models (Tables) + Relationships**

## 🎯 Goal

Design real-world DB schema

---

## 🧠 Learn (45 min)

* Tables, columns
* Primary key
* Foreign key
* One-to-many relationship

👉 DB:

* SQLite

---

## 🛠️ Build (2 hrs)

### Create Models:

* `User`
* `Post`

### Add Relationship:

* One user → many posts

---

## 🔥 Test Yourself

* Why do we use `ForeignKey`?
* What does `relationship()` do?

---

## ✅ Outcome

✔ DB schema ready
✔ Relationships working

---

# 📅 **Day 3 — Schemas (Pydantic) + Validation**

## 🎯 Goal

Separate DB layer from API layer

---

## 🧠 Learn (45 min)

* Pydantic models
* Input vs Output schemas
* Data validation

---

## 🛠️ Build (2 hrs)

### Create:

* `UserCreate`, `UserResponse`
* `PostCreate`, `PostResponse`

---

## 🔥 Test Yourself

* Why not return SQLAlchemy models directly?
* What is `from_attributes = True`?

---

## ✅ Outcome

✔ Clean API structure
✔ Safe data handling

---

# 📅 **Day 4 — CRUD Layer (Core Backend Logic)**

## 🎯 Goal

Write actual DB operations

---

## 🧠 Learn (30–45 min)

* CRUD pattern (Create, Read, Update, Delete)
* Why separation matters

---

## 🛠️ Build (2–3 hrs)

### Implement:

* `create_user`
* `create_post`
* `get_posts`
* `get_user`

---

## 🔥 Test Yourself

* Why use a CRUD layer?
* What happens if we skip it?

---

## ✅ Outcome

✔ Backend logic separated
✔ Clean architecture

---

# 📅 **Day 5 — API Routes + Dependency Injection**

## 🎯 Goal

Connect everything to FastAPI endpoints

---

## 🧠 Learn (30 min)

* Dependency Injection (`Depends`)
* How FastAPI manages DB sessions

---

## 🛠️ Build (2–3 hrs)

### Endpoints:

* Create User
* Create Post
* Get Posts
* Get User with Posts

---

## 🔥 Test Yourself

* Why use `Depends(get_db)`?
* What if DB session is global?

---

## ✅ Outcome

✔ Working backend API
✔ Proper DB session handling

---

# 📅 **Day 6 — Pagination + Filtering + Search**

## 🎯 Goal

Make API scalable (REAL WORLD)

---

## 🧠 Learn (30–45 min)

* Pagination logic
* Filtering queries

---

## 🛠️ Build (2–3 hrs)

### Pagination:

```http
GET /posts?page=1&limit=10
```

### Logic:

```python
skip = (page - 1) * limit
```

---

### Add Features:

* Filter by user_id
* Search by title
* Order by latest

---

## 🔥 Test Yourself

* Why pagination is critical?
* What happens with 1M records?

---

## ✅ Outcome

✔ Production-like API
✔ Efficient queries

---

# 📅 **Day 7 — Final Project + Polish**

## 🎯 Goal

Build a complete backend system

---

## 🛠️ Build (3–4 hrs)

### Final System:

#### 👤 Users

* Create user
* Get user with posts

#### 📝 Posts

* Create post
* Get posts (pagination)
* Filter posts

---

## 🧠 Add Improvements

### 🔥 Clean Structure

```
app/
 ├── models.py
 ├── schemas.py
 ├── crud.py
 ├── database.py
 ├── routers/
```

---

### 🔥 Optional Upgrade

* Switch to:

  * PostgreSQL

---

## 🧪 FINAL TEST (VERY IMPORTANT)

You must be able to answer:

1. How ORM works internally
2. Difference between schema & model
3. How relationships work
4. How pagination works
5. How DB session lifecycle works

---

## ✅ Final Outcome

After Day 7:

✔ You can build real backend APIs
✔ You understand DB deeply
✔ You are **internship-level backend dev**

---

# 🧠 Real Talk (Important)

If you:

* Just read → ❌ nothing happens
* Actually build daily → ✅ you level up fast

---
