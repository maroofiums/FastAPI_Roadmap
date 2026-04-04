from fastapi import FastAPI
from app.database import create_db_and_tabeles
from app.routers.auth import router as auth_router

app = FastAPI()

@app.on_event("startup")
def startup_event():
    create_db_and_tabeles()

app.include_router(auth_router, prefix="/auth", tags=["auth"])