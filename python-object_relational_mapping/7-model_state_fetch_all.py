#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    connection = "mysql+mysqldb://{}:{}@localhost:3360/{}".format(
                                                                sys.argv[1],
                                                                sys.argv[2],
                                                                sys.argv[3]
                                                                )
    # Create engine and session
    engine = create_engine(connection)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get all State objects sorted by id
    states = session.query(State).order_by(State.id).all()

    # Print the results in the expected format
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()

    session.close()
