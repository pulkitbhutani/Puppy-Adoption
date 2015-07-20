from flask import Flask , render_template, url_for , redirect , request , flash
app = Flask(__name__)

from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from puppies import Base , Shelter , Puppy

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

@app.route('/')
@app.route('/shelters/')
def showShelters():
	items = session.query(Shelter).all()
	return render_template('showShelters.html', items = items)

@app.route('/shelter/new/' , methods = ['GET', 'POST'])
def newShelter():
	if request.method == 'POST':
		newItem = Shelter(name = request.form['name1'],address = request.form['name2'], city =request.form['name3'], state = request.form['name4'], zipCode = request.form['name5'], website = request.form['name6'], maximum_capacity = request.form['name7'])
		session.add(newItem)
		session.commit()
		return redirect(url_for('showShelters'))
	else:
		return render_template('newShelter.html')


@app.route('/shelter/<int:shelter_id>/puppies/')
def showPuppies(shelter_id):
	items = session.query(Puppy).filter_by(shelter_id = shelter_id).all()
	return render_template('showPuppies.html', shelter_id = shelter_id , items = items)

@app.route('/shelter/<int:shelter_id>/checkin/', methods = ['GET', 'POST'])
def checkinPuppy(shelter_id):
	if request.method == 'POST':
		newItem = Puppy(name = request.form['name1'], gender = request.form['name2'], picture = request.form['name4'] ,shelter_id = shelter_id)
		session.add(newItem)
		session.commit()
		return redirect(url_for('showPuppies' , shelter_id = shelter_id))

	else:
		return render_template('checkinPuppy.html', shelter_id= shelter_id)

@app.route('/shelter/<int:shelter_id>/<int:puppy_id>/profile/')
def puppyProfile(shelter_id , puppy_id):
	item = session.query(Puppy).filter_by(id = puppy_id).one()
	items = session.query(Shelter).filter_by(id= shelter_id).one()
	return render_template('puppyProfile.html' , item = item , shelter_id = shelter_id, items = items ,puppy_id = puppy_id)


if __name__ == '__main__':
	app.debug = True
	app.run(host = '127.0.0.1', port = 5000)