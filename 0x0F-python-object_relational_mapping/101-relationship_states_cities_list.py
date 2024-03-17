#!/usr/bin/python3
"""lists all State objects"""
import sys
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for result in session.query(State).order_by(State.id):
        print(f"{result.id}: {result.name}")
        for city in result.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
