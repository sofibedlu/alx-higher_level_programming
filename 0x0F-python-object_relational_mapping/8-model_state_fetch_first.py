#!/usr/bin/python3

"""-script that prints the first 'State' object from the database
    'hbtn_0e_6_usa'
    -script take 3 arguments: mysql username, mysql password
    and database name
"""
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import State, Base

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(engine)

    row = session.query(State).filter(State.id == 1)
    if not row:
        print("")
    else:
        print("{}: {}".format(row[0].id, row[0].name))
    session.close()
