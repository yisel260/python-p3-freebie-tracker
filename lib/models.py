from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())
    _freebies = relationship('Freebie', backref=backref('company'))


    def __repr__(self):
        return f'<Company {self.name}>'
    
    def freebies(self):
        print(session.query(Freebie).filter(Freebie.company_id == self.id).all())
        return session.query(Freebie).filter(Freebie.company_id == self.id).all()
    
    def devs(self):
        company_freebies= Company.freebies(self)
        for freebie in company_freebies:
           print( session.query(Dev).filter(Dev.id == freebie.dev_id).all())

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())
    _freebies = relationship('Freebie', backref=backref('dev'))

    def __repr__(self):
        return f'<Dev {self.name}>'
    
    def freebies(self):
        return session.query(Freebie).filter(Freebie.dev_id == self.id).all()
    
    def companies(self):
        dev_freebies= Dev.freebies(self)
        for freebie in dev_freebies:
           print( session.query(Company).filter(Company.id == freebie.company_id).all())


    

class Freebie(Base):

    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name= Column(String())
    value = Column(Integer())
    company_id = Column(Integer(), ForeignKey("companies.id"))
    dev_id = Column(Integer(), ForeignKey("devs.id"))

    def __repr__(self):
        return f'<Freebie {self.item_name}, Value {self.value}>'
    
    def dev(self, dev_id):
        print(session.query(Freebie).filter(Freebie.dev_id == dev_id).all())
        return session.query(Freebie).filter(Freebie.dev_id == dev_id).all()

                                             
    def company(self, company_id):
        print(session.query(Freebie).filter(Freebie.company_id == company_id).all())
        return session.query(Freebie).filter(Freebie.company_id == company_id).all()
    
