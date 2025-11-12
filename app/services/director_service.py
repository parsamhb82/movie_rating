from app.repositories.director_repo import DirectorRepository
from app.schemas import director as director_schema
from app.models import models
from typing import List

class DirectorService:
    def __init__(self, director_repo: DirectorRepository):
        self.director_repo = director_repo

    def get_director(self, director_id: int) -> models.Director | None:
        return self.director_repo.get_by_id(director_id)

    def get_all_directors(self) -> List[models.Director]:
        return self.director_repo.get_all()

    def create_director(self, director_create: director_schema.DirectorCreate) -> models.Director:
        return self.director_repo.create(director_create)

    def update_director(self, director_id: int, director_update: director_schema.DirectorUpdate) -> models.Director | None:
        director = self.director_repo.get_by_id(director_id)
        if not director:
            return None
        return self.director_repo.update(director, director_update)

    def delete_director(self, director_id: int) -> bool:
        director = self.director_repo.get_by_id(director_id)
        if not director:
            return False
            
        # Add logic here later, e.g., "can't delete director with movies"
        # For now, we just delete.
            
        self.director_repo.delete(director)
        return True