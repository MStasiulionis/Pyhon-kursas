from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import SubmitField, BooleanField, StringField, PasswordField, FloatField, FileField
from wtforms.validators import DataRequired, ValidationError, EqualTo
import app


class RegistrationForm(FlaskForm):
    user_name = StringField('Vardas', [DataRequired()])
    email = StringField('El. paštas', [DataRequired()])
    password = PasswordField('Slaptažodis', [DataRequired()])
    confirm_password = PasswordField("Pakartokite slaptažodį", [EqualTo('password', "Slaptažodis turi sutapti.")])
    submit = SubmitField('Prisiregistruoti')

    def check_user_name(self, user_name):
        user = app.User.query.filter_by(user_name=user_name.data).first()
        if user:
            raise ValidationError('Šis vardas panaudotas. Pasirinkite kitą.')

    def check_email(self, email):
        user = app.User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Šis el. pašto adresas panaudotas. Pasirinkite kitą.')


class LoginForm(FlaskForm):
    email = StringField('El. paštas', [DataRequired()])
    password = PasswordField('Slaptažodis', [DataRequired()])
    remember_me = BooleanField("Prisiminti mane")
    submit = SubmitField('Prisijungti')


class DataForm(FlaskForm):
    income = BooleanField('Pajamos')
    amount = FloatField('Suma', [DataRequired()])
    submit = SubmitField('Įvesti')



