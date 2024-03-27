#!/usr/bin/env python3

from sqlalchemy import create_engine

from models import Company, Dev, Freebie
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    f1=session.query(Freebie).first()

    import ipdb; ipdb.set_trace()
