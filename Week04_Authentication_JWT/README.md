# Week 4 - Authentication & Security (Day-by-Day Plan)

## Goal of the Week

By the end of this week, you will build a **complete JWT Authentication System** with:

* User Signup
* Login
* JWT Access Token
* Protected Routes
* Password Hashing (secure)
* OAuth2 flow (industry standard)

---

# Day 1 - Project Setup + User Model

## What you build today

* Basic FastAPI project structure
* Database connection
* User model (SQLAlchemy)
* Schema setup (Pydantic)

## Tasks

### 1. Create project structure

```
app/
 ┣ core/
 ┃ ┗ security.py
 ┣ routers/
 ┃ ┗ auth.py
 ┣ crud.py
 ┣ database.py
 ┣ models.py
 ┣ schemas.py
 ┗ main.py
```

---

### 2. User Model (models.py)

Create user table:

* id
* username
* email
* hashed_password
* is_active

---

### 3. Database setup

* SQLAlchemy engine
* Session dependency

---

### 4. Schemas (schemas.py)

Create:

* UserCreate
* UserResponse
* Token
* TokenData

---

## Output of Day 1

You should have:

* Working DB connection
* User model ready
* Schema structure ready

---

# Day 2 - Password Hashing (Security Core)

## What you build today

Secure password system using:

* Passlib (bcrypt)

---

## Concepts

### Why hashing?

We NEVER store plain passwords.
We store:

```
plain_password → hash_password → database
```

---

## security.py

### 1. Hash password

* `get_password_hash(password)`

### 2. Verify password

* `verify_password(plain, hashed)`

---

## Output of Day 2

You can:

* Hash passwords
* Verify login passwords securely

---

# Day 3 - User Registration (/signup)

## What you build today

* API endpoint for user signup
* Save hashed password in DB

---

## Endpoint

```
POST /signup
```

## Flow

1. Receive user data
2. Hash password
3. Save user in database
4. Return user info (without password)

---

## CRUD function

* create_user()

---

## Output of Day 3

You can:

* Register users securely
* Store hashed passwords

---

# Day 4 - Login System + JWT Token Creation

## What you build today

* Login endpoint
* JWT token generation

---

## Key libraries

* python-jose (JWT)
* OAuth2PasswordRequestForm

---

## Endpoint

```
POST /login
```

---

## Flow

1. User enters email + password
2. Verify user
3. Check password
4. Generate JWT token

---

## JWT payload includes:

* user_id
* username
* expiry time

---

## Output of Day 4

You can:

* Login user
* Return JWT token

---

# Day 5 - Token System + Security Core Functions

## What you build today

### core/security.py

* create_access_token()
* decode token
* verify token

---

## Token Flow

```
User Login → JWT Token → Sent in Header → Backend verifies
```

---

## OAuth2 setup

```
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

---

## Output of Day 5

You have:

* JWT creation
* JWT decoding
* OAuth2 setup working

---

# Day 6 - Protected Routes

## What you build today

Secure API endpoints

---

## Example endpoint

```
GET /protected-route
```

---

## Flow

1. User sends token in header
2. Backend verifies token
3. If valid → access allowed
4. If invalid → 401 error

---

## Dependency function

```
get_current_user(token)
```

---

## Output of Day 6

You can:

* Protect routes
* Allow only authenticated users

---

# Day 7 - Final Integration + Testing

## What you do today

### Full system test:

* Signup
* Login
* Token generation
* Access protected route

---

## Testing Tools

* Swagger UI (`/docs`)
* Postman

---

## Final Flow

```
Signup → Login → Token → Protected API
```

---

## Output of Day 7

You have a complete:

# JWT Authentication System (Industry Level)

---

# Final Architecture (What you just built)

```
User
 ↓
Signup → DB (hashed password)
 ↓
Login → JWT Token
 ↓
Protected Route → Token verification
```

---

# If you want next step (important)

After this week, your next upgrade should be:

* Refresh tokens
* Role-based access (admin/user)
* OAuth Google login
* Rate limiting security

---