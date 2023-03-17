#!/usr/bin/python3

"""-a script that changes the name of a 'State' object from the
    database hbtn_0e_6_usa where 'id=2' to 'New Mexico'
    -script take 3 arguments: mysql username, mysql password
    and database name
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(engine)
    obj = session.query(State).filter_by(id=2).first()
    obj.name = 'New Mexico'
    session.commit()
    session.close()
