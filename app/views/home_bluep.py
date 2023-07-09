from flask import Blueprint, render_template

home_bluep = Blueprint('home', __name__)

@home_bluep.route("/")
def home():
    name = "Francisco Lopez"
    return render_template('home/home.html', name=name)

@home_bluep.route("/3B/")
def tres():
    alumnos = ['Gaby', 'Adriana', 'Alicia']
    return render_template('home/tres.html', alumnos=alumnos)

@home_bluep.route("/contact/")
def contact():
    user = "Frank"
    return render_template('home/contact.html', user=user)

@home_bluep.route('/about/')
def about():
    user = "Frank"
    return render_template('home/about.html', user=user)