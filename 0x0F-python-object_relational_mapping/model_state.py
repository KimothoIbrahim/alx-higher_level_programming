#!/usr/bin/pyhton3
"""script defining models/classes/tables for database"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Column


Base = declarative_base()


class State(Base):
    """ define the states table"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)
