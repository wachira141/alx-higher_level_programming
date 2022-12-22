#!/usr/bin/python3
"""print State object with the namepassed as args"""

import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = sqlalchemy.create_engine("mysql+mysqldb://{}:{}@localhost/{}".
            format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    #query py instance in db for letter a
    if session.query(State).filter_by(name=sys.argv[4]).first():
        print("{:d}".format(state.id))
    else:
        print("Not found")
    session.close()
