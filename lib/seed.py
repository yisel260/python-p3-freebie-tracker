#!/usr/bin/env python3

# Script goes here!
import random
from random import choice as rc


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Freebie, Company, Dev
from faker import Faker

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

def delete_records():
    session.query(Freebie).delete()
    session.query(Company).delete()
    session.query(Dev).delete()
    session.commit()


def create_companies():
    companies = [Company(
        name=fake.company(),
        founding_year=random.randint(1800,2023)
    ) for i in range(10)]
    session.add_all(companies)
    session.commit()
    return companies

def create_devs():
    developers = [Dev(
        name = fake.name()
    ) for i in range(50)]
    session.add_all(developers)
    session.commit()
    return developers

def create_freebies():

    freebies = [ Freebie(
        item_name =fake.word(),
        value =random.randint(0, 60),
    ) for i in range(100)]

    session.add_all(freebies)
    session.commit()
    return freebies

def relate_one_to_many(freebies, companies,devs):
    for freebie in freebies:
        freebie.dev = rc(devs)
        freebie.company= rc(companies)


    session.add_all(freebies)
    session.commit()
    return freebies,companies, devs 

if __name__ == '__main__':
    delete_records()
    companies= create_companies()
    devs = create_devs()
    freebies = create_freebies()
    relate_one_to_many(freebies,companies,devs)