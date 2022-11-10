"""
SQLAlchemy model module

Description:
    This module creates sqlalchemy models.
"""
from sqlalchemy import Column, Integer, String

from fastapi_training.my_app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    nickname = Column(String)
