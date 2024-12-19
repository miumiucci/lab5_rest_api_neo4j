from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Lab 5 - REST API with FastAPI and Neo4j")

@app.get("/")
def root():
    return {"message": "Welcome to the API! Use /docs for API documentation."}
app.include_router(router)