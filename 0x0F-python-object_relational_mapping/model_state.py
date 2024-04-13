#!/usr/bin/python3
"""
Module Start link class to table in database
"""

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String


# Define the Base class
Base = declarative_base()

if __name__ == "__main__":
    # Create an engine
    engine = create_engine(
                           'mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Define the State class
    class State(Base):
        __tablename__ = 'states'

        id = Column(Integer, primary_key=True, autoincrement=True,
                    nullable=False)
        name = Column(String(128), nullable=False)

    # Create the tables in the database
    Base.metadata.create_all(engine)
