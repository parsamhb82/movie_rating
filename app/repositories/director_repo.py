from sqlalchemy.orm import Session
from app.models import models
from app.schemas import director as director_schema

class DirectorRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, director_id: int) -> models.Director | None:
        return self.db.query(models.Director).filter(models.Director.id == director_id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[models.Director]:
        return self.db.query(models.Director).offset(skip).limit(limit).all()

    def create(self, director_create: director_schema.DirectorCreate) -> models.Director:
        db_director = models.Director(**director_create.model_dump())
        self.db.add(db_director)
        self.db.commit()
        self.db.refresh(db_director)
        return db_director

    def update(self, director: models.Director, director_update: director_schema.DirectorUpdate) -> models.Director:
        update_data = director_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(director, key, value)
            
        self.db.add(director)
        self.db.commit()
        self.db.refresh(director)
        return director

    def delete(self, director: models.Director) -> None:
        self.db.delete(director)
        self.db.commit()