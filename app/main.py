from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI(
    title="Movie Rating System API",
    description="Project for managing movies and ratings",
    version="1.0.0"
)

# A simple root endpoint to check if the server is running
@app.get("/")
def read_root():
    return {"message": "Welcome to Movie Rating API"}

app.include_router(api_router, prefix="/api/v1")