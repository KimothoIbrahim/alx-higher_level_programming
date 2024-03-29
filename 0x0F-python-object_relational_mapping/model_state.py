#!/usr/bin/pyhton3
"""script defining models/classes/tables for database"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """ define the states table"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
