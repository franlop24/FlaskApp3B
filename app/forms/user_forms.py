
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, EmailField, 
                     SubmitField, ValidationError)
from wtforms.validators import DataRequired, Email, EqualTo

from db.users import User

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                    EqualTo('password_confirm', 
                                                            message='Las contraseñas deben coincidir')])
    password_confirm = PasswordField('Password Confirm', validators=[DataRequired()])
    submit = SubmitField('Registrar')

    ######## Validar Correo Unico #########
    def validate_email(self, field):
        ######## Consultar si el correo existe en la base de datos #######
        if User.check_id(field.data):
            raise ValidationError('El correo ya existe')

    ######## Validar Username Unico #########
    def validate_username(self, field):
        ######## Consultar si el username existe en la base de datos #######
        if User.check_username(field.data):
            raise ValidationError('El username ya existe')