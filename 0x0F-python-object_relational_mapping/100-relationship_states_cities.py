#!/usr/bin/python3

"""a script that creates the 'State' “California” with the 'City'
    “San Francisco” from the database hbtn_0e_100_usa
    -script take 3 arguments: mysql username, mysql password
    and database name
"""

from sqlalchemy import create_engine
from sys import argv
from relationship_city import City, Base
from relationship_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()
