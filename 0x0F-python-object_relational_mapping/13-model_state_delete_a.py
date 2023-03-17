#!/usr/bin/python3

"""a script that deletes all 'State' objects with a name containing
    the letter 'a' from the database hbtn_0e_6_usa
    -script take 3 arguments: mysql username, mysql password and
    database name
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(engine)
    rows = session.query(State).filter(State.name.like('%a%')).all()
    for row in rows:
        session.delete(row)
    session.commit()
    session.close()
