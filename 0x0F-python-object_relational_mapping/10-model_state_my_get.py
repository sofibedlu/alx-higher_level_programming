#!/usr/bin/python3

"""a script that prints the 'State' object with the 'name' passed
    as argument from the database 'hbtn_0e_6_usa'
    -script take 4 arguments: mysql username, mysql password, database
    name and state name to search (SQL injection free)
    -Results display the 'states.id'
    -assume we have one record with the state name to search
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(engine)
    row = session.query(State).filter(State.name == argv[4]).first()
    if not row:
        print("Not found")
    else:
        print(row.id)
    session.close()
