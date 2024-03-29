#!/usr/bin/python3
"""a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa"""

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

    state = session.query(State).filter(State.id == 2).one()
    state.name = "New Mexico"
    session.commit()
