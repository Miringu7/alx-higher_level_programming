#!/usr/bin/python3
"""
Class definition of a State and an instance Base = declarative_base()
"""

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an engine
engine = create_engine('mysql://username:password@ \
                       localhost:3306/database_name')

# Define a Base class
Base = declarative_base()

# Define the State class


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# WARNING All classes that inherit from Base must be imported before
# calling Base.metadata.create_all(engine)
# For example:
# from your_module_name import State

# Create the tables in the database


Base.metadata.create_all(engine)
