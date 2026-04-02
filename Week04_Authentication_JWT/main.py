from fastapi import FastAPI
from app.database import create_db_and_tabeles

app = FastAPI()

@app.on_event("startup")
def startup_event():
    create_db_and_tabeles()