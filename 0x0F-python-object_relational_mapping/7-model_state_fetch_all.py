#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    url = ("mysql+mysqldb://{}:{}@localhost:3306/{}"
           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    engine = create_engine(url)

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id} {state.name}")
