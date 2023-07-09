from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

@error_pages.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404