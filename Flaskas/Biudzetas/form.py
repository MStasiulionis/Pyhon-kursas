from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email


class Budget(FlaskForm):
    income = IntegerField('Pajamos', [DataRequired(message='Įveskite skaičių')])
    type = SelectField(choices=[('Pajamos', 'Pajamos'), ('Išlaidos', 'Išlaidos')])
    submit = SubmitField('Submit')
