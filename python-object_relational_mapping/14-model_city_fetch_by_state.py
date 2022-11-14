#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa
"""
if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    datas = session.query(State.name, City.id, City.name).join(State, State.id == City.state_id).order_by(City.id)
    for elem in datas:
        print("{}: ({}) {}".format(elem[0], elem[1], elem[2]))
    session.close()
