#!/usr/bin/python3
""" create city table """
from sqlalchemy import String, Integer, Column, ForeignKey
from model_state import Base


class City(Base):
    """declare a city table"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
