from flask import Blueprint, render_template

from models.products import Product

product_views = Blueprint('product', __name__)

@product_views.route('/products/')
def home():
    products = Product.get_all()
    return render_template('product/products.html', products=products)