from flask import Flask, flash, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Prints the current working directory
print("Current Working Directory:", os.getcwd())

# Configure SQLite URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# SQL database user class model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # The DB table name
    __tablename__ = 'dacarhub_user_table'


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
        email = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Password and Confirm Password must match', 'danger')
        else:
            # this will create the new user objeect in the DB
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('index'))

    return render_template('regist.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == 'password' and request.form['username'] == 'admin':
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('Wrong password!')
            return render_template('login.html')
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
