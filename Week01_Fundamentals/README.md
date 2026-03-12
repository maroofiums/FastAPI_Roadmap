# **Week 1 — FastAPI Fundamentals (Day-by-Day)**

**Goal:** Understand FastAPI’s core structure, routes, Pydantic, and automatic documentation.

---

## **Day 1 — Setup & First API**

**Objectives:**

* Install FastAPI and Uvicorn
* Run your first API
* Understand ASGI vs WSGI

**Tasks:**

1. Install packages:

```bash
pip install fastapi uvicorn
```

2. Create `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
```

3. Run server:

```bash
uvicorn main:app --reload
```

4. Open Swagger docs at `http://127.0.0.1:8000/docs`

**Output / Notes:**

* Learn about **GET requests**
* Understand **how FastAPI serves endpoints**
* Observe **automatic docs**

---

## **Day 2 — Path & Query Parameters**

**Objectives:**

* Learn path vs query parameters
* Type validation

**Tasks:**

1. Add dynamic path parameter:

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

2. Add query parameter:

```python
@app.get("/search/")
def search_items(query: str = None, limit: int = 10):
    return {"query": query, "limit": limit}
```

**Notes:**

* Path params are part of URL
* Query params come after `?` in URL
* FastAPI automatically validates types

---

## **Day 3 — Request Body & Pydantic**

**Objectives:**

* Learn to accept POST data
* Introduce Pydantic for validation

**Tasks:**

1. Create `schemas.py`:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool
```

2. Update `main.py` for POST:

```python
from fastapi import FastAPI
from schemas import Item

app = FastAPI()

@app.post("/items/")
def create_item(item: Item):
    return item
```

**Notes:**

* Pydantic automatically validates incoming JSON
* Try sending invalid data to see errors

---

## **Day 4 — Response Models & Data Validation**

**Objectives:**

* Control what the API sends back
* Hide internal fields if needed

**Tasks:**

1. Update schema:

```python
class ItemResponse(BaseModel):
    name: str
    price: float
```

2. Add response model:

```python
@app.post("/items/", response_model=ItemResponse)
def create_item(item: Item):
    return item
```

**Notes:**

* Response model filters out unwanted fields
* Helps maintain API contract

---

## **Day 5 — CRUD Prep & Small Project Start**

**Objectives:**

* Understand full CRUD workflow
* Start **Item Catalog API**

**Tasks:**

* Add GET all items
* Add GET single item
* Add POST item (from Day 3 & 4)
* Use in-memory list for storage (for now)

Example:

```python
items = []

@app.get("/items/")
def list_items():
    return items

@app.post("/items/")
def add_item(item: Item):
    items.append(item)
    return item
```

**Notes:**

* No DB yet — focus on API structure
* Try multiple requests via Swagger UI

---

## **Day 6 — Project Expansion**

**Objectives:**

* Add PUT & DELETE (preparing for Week 2)
* Add optional query filters

**Tasks:**

```python
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    deleted = items.pop(item_id)
    return {"deleted": deleted.name}
```

**Notes:**

* Items stored as **list**, index as ID
* Understand API flow: request → validation → processing → response

---

## **Day 7 — Review & Notes**

**Objectives:**

* Review Week 1 concepts
* Write notes for each day
* Test API endpoints

**Tasks:**

* Check Swagger docs for all routes
* Play with query params
* Try sending invalid data to see validation errors
* Update **Week1/README.md** with notes

---

# ✅ Week 1 Deliverable

* A small **Item Catalog API** supporting:

  * GET all items
  * GET single item
  * POST item
  * PUT item
  * DELETE item
* Pydantic validation for request body
* Response models to filter fields
* Fully documented in Swagger UI
* README.md with notes