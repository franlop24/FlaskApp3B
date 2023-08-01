from flask import Blueprint, render_template

from models.products import Product

home_views = Blueprint('home',__name__)

@home_views.route("/")
def home():
    limit = 6
    products = Product.get_all(limit=limit)
    return render_template('home/home.html', products=products)

@home_views.route("/3B/")
def tres():
    alumnos = ['Gaby', 'Adriana', 'Alicia']
    return render_template('home/tres.html', alumnos=alumnos)

@home_views.route("/contact/")
def contact():
    user = "Frank"
    return render_template('home/contact.html', user=user)

@home_views.route('/about/')
def about():
    user = "Frank"
    return render_template('home/about.html', user=user)