from flask import Blueprint, render_template, redirect, url_for, abort

from forms.product_forms import CreateProductForm, UpdateProductForm

from models.products import Product
from models.categories import Category

from utils.file_handler import save_image

product_views = Blueprint('product', __name__)

@product_views.route('/products/')
def home():
    products = Product.get_all()
    return render_template('product/products.html', products=products)

@product_views.route('/products/create/', methods=('GET', 'POST'))
def create():
    form = CreateProductForm()
    categories = Category.get_all()
    cats = [(-1, '')]
    for cat in categories:
        cats.append((cat.id, cat.category))
    form.category_id.choices = cats

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        price = form.price.data
        stock = form.stock.data
        category_id = form.category_id.data
        f = form.image.data
        if f:
            image = save_image(f, 'images/products')
        product = Product(name=name, 
                          description=description,
                          price=price,
                          stock=stock,
                          category_id=category_id,
                          image=image)
        product.save()
        return redirect(url_for('product.home'))

    return render_template('product/create_product.html', form=form)

@product_views.route('/products/<int:id>/update/', methods=('GET', 'POST'))
def update(id):
    form = UpdateProductForm()
    categories = Category.get_all()
    cats = [(-1, '')]
    for cat in categories:
        cats.append((cat.id, cat.category))
    form.category_id.choices = cats
    product = Product.get(id)
    if product is None:
        abort(404)
    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        product.stock = form.stock.data
        product.category_id = form.category_id.data
        f = form.image.data
        if f:
            image = save_image(f, 'images/products')
            product.image = image
        product.save()
        return redirect(url_for('product.home'))
    form.name.data = product.name
    form.description.data = product.description
    form.price.data = product.price
    form.stock.data = product.stock
    form.category_id.data = product.category_id
    image = product.image
    return render_template('product/create_product.html', form=form, image=image)

@product_views.route('/products/<int:id>/detail/')
def detail(id):
    product = Product.get(id)
    if product is None: abort(404)
    cat = Category.get(product.category_id)
    return render_template('product/detail.html', product=product, cat=cat)