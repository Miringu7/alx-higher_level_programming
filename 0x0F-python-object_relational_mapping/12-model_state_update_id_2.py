#!/usr/bin/python3
"""Module that updates the name of a state in a\
        MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Create a session factory
    Session = sessionmaker(bind=engine)
    # Create a session object
    session = Session()

    # Retrieve the state with ID 2 from the database
    state = session.query(State).filter_by(id=2).first()
    # Update the name of the state to "New Mexico"
    state.name = "New Mexico"
    # Commit the session to persist the changes
    session.commit()
