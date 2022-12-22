#!/usr/bin/python3
"""
Define class State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """Repr a state for MySQL database
    `__tablename__ (str): The name of the MySQL table to store States.
    """
    __tablename__ = "states"
    id = Column(integer, nullabale=False, primary_key=True)
    name = Column(String(128), nullable=False)
