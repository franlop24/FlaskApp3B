from flask import Blueprint, redirect, render_template, url_for, flash

from models.users import User

from forms.user_forms import LoginForm, RegisterForm

user_views = Blueprint('user', __name__)

@user_views.route('/users/register/', methods=('GET', 'POST'))
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        user = User(username, password, email)
        user.save()

        return redirect(url_for('user.login'))
    return render_template('user/register.html', form=form)

@user_views.route('/users/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.get_by_password(username, password)
        if not user:
            flash('Verifica tus Datos')
        else:
            return render_template('home/home.html', user=user)
    return render_template('user/login.html', form=form)
