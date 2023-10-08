#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # take in arguments: mysql username, mysql password, database name
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # create engine to connect to MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(mysql_username, mysql_password, database_name))

    # create session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # query for states that contain the letter 'a' and order by states.id
    result = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    # display results
    for state in result:
        print("{}: {}".format(state.id, state.name))

    # close session
    session.close()
