#!usr/bin/python3
"""script that lists all State objects that
contain the letter a from the database"""

import sys
import sqlalchemy
import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = sqlalchemy.cretae_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    #query for letter a
    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print("{:d}: {:s}".formar(state.id, state.name)
    session.close()
