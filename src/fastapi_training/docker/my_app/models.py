"""
SQLAlchemy model module

Description:
    This module creates sqlalchemy models.
"""
from database import Base

from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    nickname = Column(String)
