from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField,TextAreaField, SelectField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileField, FileAllowed

class CreateProductForm(FlaskForm):

    cats=[]

    name = StringField('Nombre', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    price = FloatField('Precio', validators=[DataRequired(), NumberRange(min=0.0, max=None)])
    stock = IntegerField('Existencias', validators=[DataRequired(), NumberRange(min=0, max=None)])
    category_id = SelectField('Categoría', choices=cats, coerce=int, validate_choice=False, validators=[DataRequired()])
    image = FileField('Imagen de Producto', 
                      validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imagenes!')])
    submit = SubmitField('Guardar')

class UpdateProductForm(FlaskForm):

    cats = []

    name = StringField('Nombre', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    price = FloatField('Precio', validators=[DataRequired(), NumberRange(min=0.0, max=None)])
    stock = IntegerField('Existencias', validators=[DataRequired(), NumberRange(min=0, max=None)])
    category_id = SelectField('Categoría', choices=cats, coerce=int, validate_choice=False, validators=[DataRequired()])
    image = FileField('Imagen de Producto', 
                      validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo imagenes!')])
    submit = SubmitField('Actualizar')