from pydantic import BaseModel, ConfigDict
from typing import Optional

# Base schema: Common fields
class DirectorBase(BaseModel):
    name: str
    birth_year: Optional[int] = None
    description: Optional[str] = None

# Create schema: Used for POST request body
class DirectorCreate(DirectorBase):
    pass

# Update schema: Used for PUT request body
class DirectorUpdate(BaseModel):
    name: Optional[str] = None
    birth_year: Optional[int] = None
    description: Optional[str] = None

# Read schema: Used for API response
class Director(DirectorBase):
    id: int

    # Config to tell Pydantic to read from ORM models
    model_config = ConfigDict(from_attributes=True)