from flask import Flask
from flask import Flask, flash, redirect
from flask import url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from tabledef import *
import os

engine = create_engine('sqlite:///carhubmax.db', echo=True)
Session = sessionmaker(bind=engine)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


@app.route('/', endpoint='index')
def home():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return 'Favicon not found!', 404


@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/car')
def car():
    return render_template('car.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/regist', methods=['GET', 'POST'])
def regist():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Checks if the registration passwords match
        if password != confirm_password:
            flash('Password and Confirm Password must match', 'error')
            return redirect(url_for('regist'))

        # Checks if the username is already taken in the existing database
        session = Session()
        if session.query(User).filter_by(username=username).first():
            flash('Failed! Username already exists.', 'error')
            return redirect(url_for('regist'))

        # Creates a new user and add it to the database
        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('regist.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])

        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
        result = query.first()
        if result:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('Wrong password!', 'error')

    return render_template('login.html')


@app.route('/booking_1', methods=['GET', 'POST'])
def booking_1():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        mobile_number = request.form['mobile_number']
        pickup_location = request.form['pickup_location']
        drop_location = request.form['drop_location']
        pickup_date = request.form['pickup_date']
        pickup_time = request.form['pickup_time']
        adult = request.form['adult']
        child = request.form['child']
        special_request = request.form['special_request']
        payment = request.form['payment']

        session = Session()
        new_booking = CarBooking(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile_number=mobile_number,
            pickup_location=pickup_location,
            drop_location=drop_location,
            pickup_date=pickup_date,
            pickup_time=pickup_time,
            adult=adult,
            child=child,
            special_request=special_request,
            payment=payment
        )
            
        session.add(new_booking)
        session.commit()
        session.close()

        flash('Successful! Thank you for choosing CARHUB-MAX.', 'success')
        return redirect(url_for('confirmation'))
    
    return render_template('booking_1.html')


@app.route('/booking_2', methods=['GET', 'POST'])
def booking_2():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        mobile_number = request.form['mobile_number']
        pickup_location = request.form['pickup_location']
        drop_location = request.form['drop_location']
        pickup_date = request.form['pickup_date']
        pickup_time = request.form['pickup_time']
        adult = request.form['adult']
        child = request.form['child']
        special_request = request.form['special_request']
        payment = request.form['payment']

        session = Session()
        new_booking = CarBooking(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile_number=mobile_number,
            pickup_location=pickup_location,
            drop_location=drop_location,
            pickup_date=pickup_date,
            pickup_time=pickup_time,
            adult=adult,
            child=child,
            special_request=special_request,
            payment=payment
        )
            
        session.add(new_booking)
        session.commit()
        session.close()

        flash('Successful! Thank you for choosing CARHUB-MAX.', 'success')
        return redirect(url_for('confirmation'))
    
    return render_template('booking_2.html')


@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5000)
