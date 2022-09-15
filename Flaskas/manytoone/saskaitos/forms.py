from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
import app


def bank_query():
    return app.Banks.query


def person_query():
    return app.Person.query


class PersonForm(FlaskForm):
    fname = StringField('Vardas', [DataRequired()])
    lname = StringField('Pavardė', [DataRequired()])
    code = IntegerField('Asmens kodas', [DataRequired()])
    phone = IntegerField('Telefono numeris', [DataRequired()])
    submit = SubmitField('Įvesti')


class BanksForm(FlaskForm):
    bank_name = StringField('Banko pavadinimas', [DataRequired()])
    adress = StringField('Adresas', [DataRequired()])
    bank_code = IntegerField('Banko kodas', [DataRequired()])
    swift_code = IntegerField('SWIFT kodas', [DataRequired()])
    submit = SubmitField('Įvesti')


class AccountsForm(FlaskForm):
    acc_number = IntegerField('Saskaitos numeris', [DataRequired()])
    balance = IntegerField('Sąskaitos balansas', [DataRequired()])
    bank = QuerySelectField(query_factory=bank_query, allow_blank=True, get_label="bank_name")
    person = QuerySelectField(query_factory=person_query, allow_blank=True, get_label="code")
    submit = SubmitField('Įvesti')
