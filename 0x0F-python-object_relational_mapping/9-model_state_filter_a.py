#!/usr/bin/python3

"""script that lists all 'State' objects that contain the letter 'a'
    from the database 'hbtn_0e_6_usa'
    - script should take 3 arguments: mysql username, mysql password
    and database name
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)
    rows = session.query(State).order_by(State.id).all()
    for row in rows:
        if 'a' in row.name:
            print("{}: {}".format(row.id, row.name))
    session.close()
