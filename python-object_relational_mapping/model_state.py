#!/usr/bin/python3
"""
state class and Base, an instance of declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    contains the class definition of a State and an instance
    Base = declarative_base() with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                auto_increment=True, nullable=False)
    name = Column(String(128), nullable=False)
