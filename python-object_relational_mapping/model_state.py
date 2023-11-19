#!/usr/bin/python3
"""
    Class State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """

    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, unique=True, nullable=True,
    primary_key=True)
    name = Column(String(128), nullable=True)
