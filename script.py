from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from puppies import Base , Shelter , Puppy

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

def allot():
	item = session.query(Puppy).all()
	for items in item:
		things = session.query(Shelter).all()
		for thing in things:
			if items.shelter_id == thing.id:
				thing.current_occupancy = thing.current_occupancy + 1
				session.add(thing)
				session.commit()

allot()