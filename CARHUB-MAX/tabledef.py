from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///carhubmax.db', echo=True)
Base = declarative_base()


class User(Base):
    """creates a new user"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    
    
    def __init__(self, username, password):
        """defines the user data"""
        self.username = username
        self.password = password


class CarBooking(Base):
    __tablename__ = 'car_bookings'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    mobile_number = Column(String)
    pickup_location = Column(String)
    drop_location = Column(String)
    pickup_date = Column(String)
    pickup_time = Column(String)
    adult = Column(String)
    child = Column(String)
    special_request = Column(String)
    payment = Column(String)
    

# This should create a table
Base.metadata.create_all(engine)
