#settings.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # This will create a file named 'movie.db' in your project's root
    DATABASE_URL: str = "sqlite:///./movie.db" 

    class Config:
        env_file = ".env"

settings = Settings()

