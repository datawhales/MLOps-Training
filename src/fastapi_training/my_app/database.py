"""
ORM Setup module

Description:
    This module setups orm using sqlalchemy.
    
    The module works as follows.
    
    1. Prepares connection to db using engine.
    2. Creates database session class.
    3. Creates base class for orm models.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up DB configuration
config = {
    "user": "postgres",
    "password": "apipassword",
    "host": "172.25.0.245",
    "port": 5433,
    "database": "apidatabase",
}

SQLALCHEMY_DATABASE_URL = f"postgresql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"

engine = create_engine(url=SQLALCHEMY_DATABASE_URL)

# Class of database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for ORM models
Base = declarative_base()
