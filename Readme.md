# **FastAPI Learning Plan – Week-by-Week (7 Weeks)**

---

# Week 1 — FastAPI Fundamentals

### Goals

* Understand FastAPI core architecture
* Understand request/response lifecycle
* Learn **Pydantic validation**
* Explore automatic documentation

### Topics

* Installing **FastAPI**
* Running server with **Uvicorn**
* GET and POST endpoints
* Path parameters
* Query parameters
* Request body validation
* Response models
* Swagger / OpenAPI documentation

### Build

**Item / Product Catalog API**

Endpoints

```
GET /items
GET /items/{id}
POST /items
```

### Key Concept

Request → Validation → Processing → Response

### Resources

FastAPI Official Tutorial
Traversy Media FastAPI Crash Course

---

# Week 2 — CRUD + Routers + Project Structure

### Goals

* Master CRUD APIs
* Structure a backend project
* Learn modular routing

### Topics

* PUT & DELETE methods
* APIRouter
* Request vs response models
* Optional parameters
* Data validation

### Project Structure

```
app
 ├── main.py
 ├── routers
 │    └── posts.py
 ├── schemas
 │    └── post.py
 ├── models
 │    └── post.py
 └── services
      └── post_service.py
```

### Build

**Blog API**

Endpoints

```
GET /posts
GET /posts/{id}
POST /posts
PUT /posts/{id}
DELETE /posts/{id}
```

Features

* Response models
* Hide internal DB fields

---

# Week 3 — Database Integration

### Goals

* Persist data in database
* Learn ORM concepts

### Topics

* **SQLAlchemy**
* SQLite/PostgreSQL database
* Dependency injection for DB sessions
* ORM models
* One-to-many relationships
* Pagination & filtering

### Build

**Users + Posts system**

Models

```
User
Post
```

Relationship

```
User → many Posts
```

### Example Endpoint

```
GET /posts?page=1&limit=10
```

---

# Week 4 — Authentication & Security

### Goals

* Build secure authentication system
* Protect API endpoints

### Topics

* Password hashing with **Passlib**
* OAuth2 authentication
* JWT tokens using **python-jose**
* Token authentication
* Protected routes

### Key Components

```
/signup
/login
/token
/protected-route
```

### Build

**JWT Auth System**

Features

* User registration
* Login
* Access token
* Protected endpoints

---

# Week 5 — Async Programming & Background Tasks

### Goals

* Understand asynchronous APIs
* Use background processing

### Topics

* async / await
* Non-blocking I/O
* BackgroundTasks
* Async HTTP calls using **HTTPX**
* Async database drivers

### Build

**External Data Fetch API**

Example

```
GET /weather
```

Flow

```
API → external API → store result in database
```

Also build

**Email simulation system**

```
POST /send-email
```

Runs in background task.

---

# Week 6 — Testing & Configuration

### Goals

* Write automated tests
* Manage configuration securely

### Topics

* Testing with **pytest**
* FastAPI TestClient
* Dependency overrides
* Environment variables
* `.env` files
* Config management with Pydantic BaseSettings

### Build

Write tests for

```
auth routes
CRUD routes
database operations
```

---

# Week 7 — Docker + Deployment

### Goals

* Containerize application
* Deploy backend to cloud

### Topics

* Dockerfile
* docker-compose
* Production servers
* Logging
* CI/CD pipelines

### Tools

* **Docker**
* **GitHub Actions**

### Deployment Options

* **Render**
* **Fly.io**
* **DigitalOcean**

### Build

Deploy your **Blog + Auth API**.

---

# Final Project (Very Important)

Instead of separate projects, build **one evolving project**:

### Week progression

Week 1
Basic API

Week 2
Blog CRUD API

Week 3
Add database

Week 4
Add authentication

Week 5
Add async features

Week 6
Add tests

Week 7
Docker + deploy

Result:

**Production-ready backend project**

---

# Advanced Topics 

Learn these next:

* Dependency injection system
* Redis caching
* Rate limiting
* WebSockets
* API versioning
* Microservices
* Event queues (RabbitMQ / Kafka)

---

# Perfect Project for You (ML + Backend)

Since you're learning ML, build:

### ML Prediction API

Example

```
POST /predict
POST /train
GET /models
```

FastAPI is widely used for **ML model serving**.

---
