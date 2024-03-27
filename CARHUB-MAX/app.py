from flask import Flask
from flask import Flask, flash, redirect, url_for, render_template, request, session
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


@app.route('/booking_1')
def booking_1():
    return render_template('booking_1.html')


@app.route('/booking_2')
def booking_2():
    return render_template('booking_2.html')


@app.route('/booking_3')
def booking_3():
    return render_template('booking_3.html')


@app.route('/booking_6')
def booking_6():
    return render_template('booking_6.html')


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
            flash('Username already exists. Please choose a different one.', 'error')
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


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5000)
