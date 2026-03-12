from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return {"msg":"Hello"}

@app.get("/ping")
def pong():
    return {"msg":"pong"}

@app.get("/health")
def healthy():
    return {"msg":"healthy"}