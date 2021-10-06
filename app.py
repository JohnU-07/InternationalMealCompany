# from flask import (
#     Flask,
#     g,
#     redirect,
#     render_template,
#     request,
#     session,
#     url_for
# )

# class User:
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password

#     def __repr__(self):
#         return f'<User: {self.username}>'

# users = []
# users.append(User(id=1, username='Anthony', password='password'))
# users.append(User(id=2, username='Becca', password='secret'))
# users.append(User(id=3, username='Carlos', password='somethingsimple'))


# app = Flask(__name__)
# app.secret_key = 'somesecretkeythatonlyishouldknow'

# @app.before_request
# def before_request():
#     g.user = None

#     if 'user_id' in session:
#         user = [x for x in users if x.id == session['user_id']][0]
#         g.user = user
        

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session.pop('user_id', None)

#         username = request.form['username']
#         password = request.form['password']
        
#         user = [x for x in users if x.username == username][0]
#         if user and user.password == password:
#             session['user_id'] = user.id
#             return redirect(url_for('profile'))

#         return redirect(url_for('login'))

#     return render_template('login.html')

# @app.route('/profile')
# def profile():
#     if not g.user:
#         return redirect(url_for('login'))

#     return render_template('profile.html')


#---------------------------------------------------------
# import the Flask class from the flask module

from flask import Flask, redirect, render_template, request, url_for, session, flash
from functools import wraps
import os


# create the application object
app = Flask(__name__)

app.secret_key = os.urandom(16)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Para continuar es necesario que inicie sesión.')
            return redirect(url_for('login'))
    return wrap


# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    # return "Hello, World!"  # return a string
    return render_template('index.html')  # render a template

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        # Change username and password to test
        if username != 'admin' or password != 'admin':
            error = 'Credenciales invalidas. Por favor intente de nuevo.'
        else:
            session['logged_in'] = True
            flash('Usuario Logueado!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('Usuario Deslogueado!')
    return redirect(url_for('welcome'))

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
