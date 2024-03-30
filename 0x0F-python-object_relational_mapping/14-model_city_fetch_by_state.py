#!/usr/bin/python3
"""join states and cities tables"""

from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    url = ("mysql+mysqldb://{}:{}@localhost:3306/{}"
           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (session.query(State.name, City.id, City.name)
              .filter(State.id == City.state_id).all())

    for instance in cities:
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])
