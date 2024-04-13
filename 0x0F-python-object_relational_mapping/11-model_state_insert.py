#!/usr/bin/python3
"""Module that adds a new state to a MySQL database using SQLAlchemy."""
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

    # Create a new State object for Louisiana
    louisiana = State(name="Louisiana")
    # Add the new state to the session
    session.add(louisiana)
    # Commit the session to persist the changes
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    # Print the ID of the newly added state
    print(new_instance.id)
    session.commit()
