from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.core.db import Base  # Import our Base from db.py

# This is the association table for the Movie <-> Genre Many-to-Many
movie_genres_association = Table(
    'movie_genres', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True)
)

class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    birth_year = Column(Integer)
    description = Column(String)

    # This 'movies' field is the list of Movie objects
    # related to this Director
    movies = relationship("Movie", back_populates="director")

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String)

    movies = relationship(
        "Movie",
        secondary=movie_genres_association,
        back_populates="genres"
    )

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    release_year = Column(Integer, index=True)
    cast = Column(String)
    
    # Foreign Key to Director
    director_id = Column(Integer, ForeignKey('directors.id'), nullable=False)
    
    # The 'director' field is a single Director object
    director = relationship("Director", back_populates="movies")

    # The 'genres' field is a list of Genre objects
    genres = relationship(
        "Genre",
        secondary=movie_genres_association,
        back_populates="movies"
    )
    
    # The 'ratings' field is a list of MovieRating objects
    ratings = relationship("MovieRating", back_populates="movie", cascade="all, delete-orphan")

class MovieRating(Base):
    __tablename__ = "movie_ratings"
    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer, nullable=False)
    
    # Foreign Key to Movie
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    
    # The 'movie' field is a single Movie object
    movie = relationship("Movie", back_populates="ratings")