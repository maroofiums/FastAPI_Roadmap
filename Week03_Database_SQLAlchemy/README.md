# Week 3 — Database Integration (Day-by-Day Plan)

Goal: Move from “API without memory” → “real backend with persistent database, ORM, and relations”

---

## Day 1 — ORM Foundations (SQLAlchemy Basics)

Focus:

* What is ORM (Object Relational Mapping)
* Difference: raw SQL vs ORM
* SQLAlchemy setup concept (engine, session, base)

Learn:

* Models = Python classes → database tables
* Session = connection manager (talks to DB)

Build:

* Simple “User” model design (no relationships yet)
* Understand table → class mapping

Task:

* Draw mental mapping:
  Python class → table → row → column

---

## Day 2 — Database Setup + Dependency Injection

Focus:

* SQLite / PostgreSQL connection
* Session lifecycle in FastAPI
* Dependency Injection (DI)

Learn:

* Why we don’t keep DB session global
* Request → open session → use → close

Build:

* DB connection layer design
* “get_db” dependency concept

Task:

* Understand flow:
  Request → Dependency → Session → Query → Close

---

## Day 3 — ORM Models (User + Post)

Focus:

* Real schema design

Learn:

* User table fields (id, name, email)
* Post table fields (id, title, content, user_id)

Build:

* Define both models conceptually
* Primary key vs foreign key

Task:

* Visual schema:
  User (1) → Post (many)

---

## Day 4 — Relationships (One-to-Many)

Focus:

* Core relational database concept

Learn:

* Foreign key role
* Relationship mapping (User ↔ Posts)
* back_populates concept (bidirectional link)

Build:

* Understand:

  * User.posts
  * Post.user

Task:

* Trace data flow:
  “One user creates many posts”

---

## Day 5 — CRUD with ORM

Focus:

* Database operations using ORM

Learn:

* Create / Read / Update / Delete using session
* Query patterns

Build:

* User CRUD
* Post CRUD (linked to user)

Task:

* Practice mental flow:
  API → service → ORM → DB → response

---

## Day 6 — Pagination + Filtering (Real API Behavior)

Focus:

* Production-style APIs

Learn:

* limit / offset pagination
* query parameters
* filtering by user_id

Example behavior:

* GET /posts?page=1&limit=10
* GET /posts?user_id=3

Build:

* Paginated post listing logic

Task:

* Understand:
  Why real APIs never return “all data”

---

## Day 7 — Mini Project Integration (Users + Posts System)

Focus:

* Combine everything

Build:

* FastAPI app with:

  * User endpoints
  * Post endpoints
  * Relationships working
  * Pagination working

Final Outcome:
You will have:

* Real database-backed API
* ORM-based architecture
* Clean scalable backend structure

---
