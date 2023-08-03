from flask import Blueprint, render_template

from models.products import Product
from models.categories import Category

from forms.home_forms import CategoryForm

home_views = Blueprint('home',__name__)

@home_views.route("/", methods=['GET', 'POST'])
def home():
    # Recupara categorias
    categories = Category.get_all()
    # Crea una lista con categorias para el Select
    cats = [('-1', 'Todos')]
    for category in categories:
        cats.append((category.id, category.category))
    # Crea instancia de Formulario
    form = CategoryForm()
    # Envía la lista al Select
    form.categories.choices = cats
    # Envía productos de categoria seleccionada al home
    if form.validate_on_submit():
        cat_id = form.categories.data
        if cat_id == -1:
            products = Product.get_all(limit=6)
        else:
            products = Product.get_by_category(cat_id)
        form.categories.data = cat_id
        return render_template('home/home.html', products=products, cats=cats, form=form)
    # Si no ha sido presionado Buscar envía todos los productos
    products = Product.get_all(limit=6)
    return render_template('home/home.html', products=products, cats=cats, form=form)

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