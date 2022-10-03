from flask_login import LoginManager, UserMixin, current_user, logout_user, login_user, login_required
import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite?check_same_thread=False')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'register'
login_manager.login_message_category = 'info'


class Vartotojas(db.Model, UserMixin):
    __tablename__ = "vartotojas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String(20), unique=True, nullable=False)
    el_pastas = db.Column("El. pašto adresas", db.String(120), unique=True, nullable=False)
    slaptazodis = db.Column("Slaptažodis", db.String(60), unique=True, nullable=False)


class RegistracijosForma(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    el_pastas = StringField('El. paštas', [DataRequired()])
    slaptazodis = PasswordField('Slaptažodis', [DataRequired()])
    patvirtintas_slaptazodis = PasswordField("Pakartokite slaptažodį", [EqualTo('slaptazodis', "Slaptažodis turi sutapti.")])
    submit = SubmitField('Prisiregistruoti')

    def tikrinti_varda(self, vardas):
        vartotojas = Vartotojas.query.filter_by(vardas=vardas.date).first()
        if vartotojas:
            raise ValidationError('Šis vardas panaudotas. Pasirinkite kitą.')

    def tikrinti_pasta(self, el_pastas):
        vartotojas = Vartotojas.query.filter_by(el_pastas=el_pastas.date).first()
        if vartotojas:
            raise ValidationError('Šis el. pašto adresas panaudotas. Pasirinkite kitą.')


class PrisijungimoForma(FlaskForm):
    el_pastas = StringField('El. paštas', [DataRequired()])
    slaptazodis = PasswordField('Slaptažodis', [DataRequired()])
    prisiminti = BooleanField("Prisiminti mane")
    submit = SubmitField('Prisijungti')


@login_manager.user_loader
def load_user(vartotojo_id):
    return Vartotojas.query.get(int(vartotojo_id))


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/logout")
def atsijungti():
    logout_user()
    return redirect(url_for('index'))


@app.route("/register", methods=['GET', 'POST'])
def registruotis():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistracijosForma()
    if form.validate_on_submit():
        koduotas_slaptazodis = generate_password_hash(form.slaptazodis.data)
        vartotojas = Vartotojas(vardas=form.vardas.data, el_pastas=form.el_pastas.data, slaptazodis=koduotas_slaptazodis)
        db.session.add(vartotojas)
        db.session.commit()
        flash('Sėkmingai prisiregistravote! Galite login', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def prisijungti():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = PrisijungimoForma()
    if form.validate_on_submit():
        user = Vartotojas.query.filter_by(el_pastas=form.el_pastas.data).first()
        if user and check_password_hash(user.password, form.slaptazodis.data):
            login_user(user, remember=form.prisiminti.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Prisijungti nepavyko. Patikrinkite el. paštą ir slaptažodį', 'danger')
    return render_template('login.html', title='Prisijungti', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    db.create_all()
