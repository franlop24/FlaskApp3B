from flask import Flask

# Import from Views
from views.home_views import home_views
from views.category_views import category_views
from views.user_views import user_views
from views.error_views import error_views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'

app.register_blueprint(home_views)
app.register_blueprint(category_views)
app.register_blueprint(user_views)
app.register_blueprint(error_views)

if __name__ == '__main__':
    app.run(debug=True)