#!/usr/bin/python3
""" changes the name of a State from the database"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(db_username, db_password, db_name))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    stateUpdate = session.query(State).filter_by(id=2).first()
    if stateUpdate:
        stateUpdate.name = "New Mexico"

    session.commit()
    session.close()
