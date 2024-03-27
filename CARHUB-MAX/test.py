import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///carhubmax.db', echo=True)

# creates a new Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin", "password")
session.add(user)

user = User("joel", "password")
session.add(user)

user = User("olagoke", "password")
session.add(user)

# commit the record the database
session.commit()

session.commit()
