#!/usr/bin/python3

"""script that prints all 'City' objects from the database hbtn_0e_14_usa
    -script take 3 arguments: mysql username, mysql password and
    database name
"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(engine)

    rows = session.query(State, City).filter(State.id == City.state_id).\
        order_by(City.id)
    for state, city in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
