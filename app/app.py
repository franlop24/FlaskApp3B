from flask import (Flask, render_template, request,
                   redirect, url_for, flash)

# import from Database
from db.categories import Category
from db.users import User

# import from Forms
from forms.user_forms import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'

@app.route("/")
def home():
    name = "Francisco Lopez"
    return render_template('home.html', name=name)

@app.route("/3B/")
def tres():
    alumnos = ['Gaby', 'Adriana', 'Alicia']
    return render_template('tres.html', alumnos=alumnos)

@app.route("/contact/")
def contact():
    user = "Frank"
    return render_template('contact.html', user=user)

@app.route('/about/')
def about():
    user = "Frank"
    return render_template('about.html', user=user)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@app.route('/categories/')
def categories():
    # Consultas Categorias de DB
    categories = Category.get_all()
    return render_template('categories.html', 
                           categories=categories)

@app.route('/categories/create/', methods=('GET', 'POST'))
def create_cat():
    if request.method == 'POST':
        # Cuando demos click en Guardar
        category = request.form['category']
        description = request.form['description']
        if not category:
            flash('Debes ingresar la categoria')
        elif not description:
            flash('Debes ingresar la description')
        else:
            cat = Category(category, description)
            cat.save()
            return redirect(url_for('categories'))

    return render_template('create_cat.html')

@app.route('/categories/<int:id>/update/')
def update_cat(id):
    return "Vamos a Actualizar"

@app.route('/categories/<int:id>/delete/')
def delete_cat(id):
    cat = Category.get(id)
    cat.delete()
    return redirect(url_for('categories'))

@app.route('/users/register/', methods=('GET', 'POST'))
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        user = User(username, password, email)
        user.save()

        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/users/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.get_by_password(username, password)
        if not user:
            flash('Verifica tus Datos')
        else:
            return render_template('home.html', user=user)
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)