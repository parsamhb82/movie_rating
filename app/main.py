from fastapi import FastAPI

app = FastAPI(
    title="Movie Rating System API",
    description="Project for managing movies and ratings",
    version="1.0.0"
)

# A simple root endpoint to check if the server is running
@app.get("/")
def read_root():
    return {"message": "Welcome to Movie Rating API"}

# We will add our API router here later
# ...