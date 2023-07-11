from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CreateCategoryForm(FlaskForm):
    category = StringField('Categoría',
                           validators=[DataRequired(),
                                       Length(min=3, max=30)])
    description = TextAreaField('Descripción', 
                                validators=[DataRequired()])
    submit = SubmitField('Guardar')

class UpdateCategoryForm(FlaskForm):
    category = StringField('Categoría',
                           validators=[DataRequired(),
                                       Length(min=3, max=30)])
    description = TextAreaField('Descripción', 
                                validators=[DataRequired()])
    submit = SubmitField('Actualizar')