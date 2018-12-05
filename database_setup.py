import sys
from sqlalchemy import Column , ForeignKey , Integer , String
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

class Company(Base):
    __tablename__ = 'company'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):

        return {
            'name': self.name,
            'id': self.id
            }


class MobilePhones(Base):
    __tablename__ = 'mobile_phones'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    Specifications = Column(String(250))
    price = Column(String(8))
    company_id = Column(Integer, ForeignKey('company.id'))
    company = relationship(Company)

    @property
    def serialize(self):

        return {
            'name': self.name,
            'Specifications': self.Specifications,
            'id': self.id,
            'price': self.price,
        }



engine = create_engine('sqlite:///mobilephones.db')
Base.metadata.create_all(engine)
