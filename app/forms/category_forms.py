from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CreateCategory(FlaskForm):
    category = StringField('Categoría', validators=[DataRequired()])
    description = TextAreaField('Descripción')
    submit = SubmitField('Guardar')

class UpdateCategory(FlaskForm):
    category = StringField('Categoría', validators=[DataRequired()])
    description = TextAreaField('Descripción')
    submit = SubmitField('Actualizar')