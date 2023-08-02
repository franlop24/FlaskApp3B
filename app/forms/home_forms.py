from flask_wtf import FlaskForm

from wtforms import SelectField, SubmitField

class CategoryForm(FlaskForm):
    categories = SelectField('Selecciona Categoría', choices=[], coerce=int, validate_choice=False)
    submit = SubmitField('Buscar')
