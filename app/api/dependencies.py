from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.repositories.director_repo import DirectorRepository
from app.services.director_service import DirectorService

def get_director_repository(db: Session = Depends(get_db)) -> DirectorRepository:
    return DirectorRepository(db)

def get_director_service(
    repo: DirectorRepository = Depends(get_director_repository)
) -> DirectorService:
    return DirectorService(repo)