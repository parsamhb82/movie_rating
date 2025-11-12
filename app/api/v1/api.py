from fastapi import APIRouter
from app.api.v1 import directors

api_router = APIRouter()
api_router.include_router(directors.router)
# When we add genres, we'll import and include it here