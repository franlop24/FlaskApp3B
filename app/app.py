from flask import Flask

# Import from blueprints
from views.home_bluep import home_bluep
from views.category_bluep import category_bluep
from views.users_bluep import user_bluep
from views.errors_blue import error_pages

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'

app.register_blueprint(home_bluep)
app.register_blueprint(category_bluep)
app.register_blueprint(user_bluep)
app.register_blueprint(error_pages)

if __name__ == '__main__':
    app.run(debug=True)