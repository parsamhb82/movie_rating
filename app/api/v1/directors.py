from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.services.director_service import DirectorService
from app.schemas import director as director_schema
from app.api.dependencies import get_director_service

router = APIRouter(
    prefix="/directors",  # URL prefix for all routes in this file
    tags=["Directors"]      # Grouping in the /docs
)

@router.post("/", response_model=director_schema.Director, status_code=status.HTTP_201_CREATED)
def create_new_director(
    director_in: director_schema.DirectorCreate,
    service: DirectorService = Depends(get_director_service)
):
    return service.create_director(director_in)

@router.get("/", response_model=List[director_schema.Director])
def get_all_directors(
    service: DirectorService = Depends(get_director_service)
):
    return service.get_all_directors()

@router.get("/{director_id}", response_model=director_schema.Director)
def get_director_by_id(
    director_id: int,
    service: DirectorService = Depends(get_director_service)
):
    director = service.get_director(director_id)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    return director

@router.put("/{director_id}", response_model=director_schema.Director)
def update_existing_director(
    director_id: int,
    director_in: director_schema.DirectorUpdate,
    service: DirectorService = Depends(get_director_service)
):
    director = service.update_director(director_id, director_in)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    return director

@router.delete("/{director_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_director(
    director_id: int,
    service: DirectorService = Depends(get_director_service)
):
    success = service.delete_director(director_id)
    if not success:
        raise HTTPException(status_code=404, detail="Director not found")
    return None