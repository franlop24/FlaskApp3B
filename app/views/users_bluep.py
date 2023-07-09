from flask import Blueprint, render_template, redirect, url_for, flash, abort

from models.users import User

from forms.user_forms import RegisterForm, LoginForm, ProfileForm

from utils.file_handler import save_image

user_bluep = Blueprint('user', __name__)

@user_bluep.route('/users/register/', methods=('GET', 'POST'))
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        user = User(username, password, email)
        user.save()

        return redirect(url_for('user.login'))
    return render_template('users/register.html', form=form)

@user_bluep.route('/users/login/', methods=('GET', 'POST'))
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
    return render_template('users/login.html', form=form)

@user_bluep.route('/users/<int:id>/profile/', methods=('GET', 'POST'))
def profile(id):
    form = ProfileForm()
    user = User.__get__(id)
    if not user:
        abort(404)
    if form.validate_on_submit():
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        f = form.image.data
        if f:
            user.image = save_image(f, 'images/profiles', user.username)
        user.save()
    form.first_name.data = user.first_name
    form.last_name.data = user.last_name
    image = user.image
    return render_template('users/profile.html', form=form, image=image)