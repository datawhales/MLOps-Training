"""
ORM Setup module

Description:
    This module setups orm using sqlalchemy.
    
    The module works as follows.
    
    1. Prepares connection to db using engine.
    2. Creates database session class.
    3. Creates base class for orm models.
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv(
    key="SQLALCHEMY_DATABASE_URL",
    default="postgresql://userforapi:pwforapi@localhost:5432/dbforapi",
)

# Create engine
engine = create_engine(url=SQLALCHEMY_DATABASE_URL)

# Create class of database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()
