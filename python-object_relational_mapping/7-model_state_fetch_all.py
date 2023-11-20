#!/usr/bin/python3
"""
    Script that lists all State objects from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name_ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1],
        atgv[2],
        argv[3]
    ))

    sess = sessionmaker(bind=engine)
    Session = sess()
    session = Session()
    result = session.query(State).order_by(State.id)

    for resu in result:
        print(resu)
