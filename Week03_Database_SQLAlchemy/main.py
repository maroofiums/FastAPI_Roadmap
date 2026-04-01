from app.routers.users import router as users_router
from app.routers.posts import router as posts_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(users_router)
app.include_router(posts_router)

@app.on_event("startup")
def on_startup():
    from app.database import create_db_and_tables
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/ping")
def ping():
    return {"message": "pong"}