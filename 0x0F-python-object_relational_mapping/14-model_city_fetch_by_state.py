#!/usr/bin/python3
"""
Module that retrieves and prints a list of cities with their
associated states from a MySQL database using SQLAlchemy.
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    # Create a session factory
    Session = sessionmaker(bind=engine)
    # Create a session object
    session = Session()
    # Retrieve cities and their associated states from the database
    # by joining the City and State tables based on the state_id
    # and ordering the results by city ID
    for instance in session.query(State.name, City.id, City.name) \
                              .filter(State.id == City.state_id) \
                              .order_by(City.id):
        # Print the city and state information
        print(instance[0] +": (" + str(instance[1]) + ") " + instance[2])

