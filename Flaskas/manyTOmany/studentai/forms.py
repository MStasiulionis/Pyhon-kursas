from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
# from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
import app


class TevasForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    vaikai = QuerySelectMultipleField(query_factory=Vaikas.query.all, get_label="vardas")
    submit = SubmitField('Įvesti')


class VaikasForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    tevai = QuerySelectMultipleField(query_factory=Tevas.query.all, get_label="vardas")
    submit = SubmitField('Įvesti')
