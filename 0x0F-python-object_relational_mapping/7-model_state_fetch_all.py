#!/usr/bin/python3

"""a script that lists all 'State' objects from the database 'hbtn_0e_6_usa'
    -script take 3 arguments: mysql username,
    mysql password and database name
"""

from model_state import State, Base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(engine)

    rows = session.query(State).order_by(State.id).all()
    for row in rows:
        print("{}: {}".format(row.id, row.name))

    session.close()
