from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, ValidationError


def status_check(form, field):
    if field.data != 'published' and field.data != 'unpublished':
        raise ValidationError(f"Field must either published or unpublished")


class ProductForm(FlaskForm):
    product_name = StringField('Product name', validators=[DataRequired()])
    product_price = FloatField('Price', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired(), status_check])
    submit = SubmitField('submit')
