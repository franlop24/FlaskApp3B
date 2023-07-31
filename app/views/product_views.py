from flask import Blueprint, render_template, redirect, url_for

from forms.product_forms import CreateProductForm

from models.products import Product

from utils.file_handler import save_image

product_views = Blueprint('product', __name__)

@product_views.route('/products/')
def home():
    products = Product.get_all()
    return render_template('product/products.html', products=products)

@product_views.route('/products/create/', methods=('GET', 'POST'))
def create():
    form = CreateProductForm()

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