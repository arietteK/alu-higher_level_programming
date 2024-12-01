#!/usr/bin/python3
"""List all states from the database and delete those containing 'a' in their name"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).all()
    print(f"Found {len(states)} states to delete:")
    for state in states:
        print(f"State to delete: {state.id} - {state.name}")
    
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
