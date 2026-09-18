
from tokenize import String
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Float, String, Integer

Base= declarative_base()

class Product(Base):

    __tablename__='product'

    id = Column(Integer,primary_key=True,index=True)
    name=Column(String)
    description=Column(String)
    price=Column(Float)
    quantity=Column(Integer)