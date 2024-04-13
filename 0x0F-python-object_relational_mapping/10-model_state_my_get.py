#!/usr/bin/python3
"""Module that searches for a state in a MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Search for the specified state in the database
    instance = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(instance[0].id)
    # Print a message if the state is not found
    if found is False:
        print("Not found")
