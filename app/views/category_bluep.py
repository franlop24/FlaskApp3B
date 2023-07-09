from flask import Blueprint, render_template, redirect, url_for, request

from models.categories import Category

from forms.category_forms import CreateCategory, UpdateCategory

category_bluep = Blueprint('category', __name__)

@category_bluep.route('/categories/')
def categories():
    # Consultas Categorias de DB
    categories = Category.get_all()
    return render_template('categories/categories.html', 
                           categories=categories)

@category_bluep.route('/categories/create/', methods=('GET', 'POST'))
def create_cat():
    form = CreateCategory()

    if form.validate_on_submit():
        category = form.category.data
        description = form.description.data
        cat = Category(category, description)
        cat.save()
        return redirect(url_for('category.categories'))

    return render_template('categories/create_cat.html', form=form)

@category_bluep.route('/categories/<int:id>/update/', methods=('GET', 'POST'))
def update_cat(id):
    form = UpdateCategory()
    cat = Category.get(id)
    if form.validate_on_submit():
        cat.category = form.category.data
        cat.description = form.description.data
        cat.save()
        return redirect(url_for('category.categories'))
    form.category.data = cat.category
    form.description.data = cat.description
    return render_template('categories/create_cat.html', form=form)
        

@category_bluep.route('/categories/delete/', methods=('POST',))
def delete_cat():
    cat_id = request.form['cat_id']
    cat = Category.get(cat_id)
    cat.delete()
    return redirect(url_for('category.categories'))