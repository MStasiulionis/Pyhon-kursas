import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, UserMixin, current_user, logout_user, login_user, login_required
from sqlalchemy import DateTime
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

import forms

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '4654f5dfadsrfasdr54e6rae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'biudzetas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = "Prisijunkite, jei norite matyti puslapį."


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column("Vardas", db.String(20), unique=True, nullable=False)
    email = db.Column("El. pašto adresas", db.String(120), unique=True, nullable=False)
    password = db.Column("Slaptažodis", db.String(60), unique=True, nullable=False)
    avatar = db.Column(db.String(20), nullable=False, default='default.jpg')


class UserData(db.Model):
    __tablename__ = "irasas"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column("Data", DateTime, default=datetime.now())
    income = db.Column("Pajamos", db.Boolean)
    amount = db.Column("Dydis", db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", lazy=True)


@login_manager.user_loader
def load_user(user_id):
    db.create_all()
    return User.query.get(int(user_id))


@app.route("/register", methods=['GET', 'POST'])
def register():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        password_hash = generate_password_hash(form.password.data)
        user = User(user_name=form.user_name.data, email=form.email.data, password=password_hash)
        db.session.add(user)
        db.session.commit()
        flash('Sėkmingai prisiregistravote! Galite login', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Prisijungti nepavyko. Patikrinkite el. paštą ir slaptažodį', 'danger')
    return render_template('login.html', title='Prisijungti', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Paskyra')


@app.route("/admin")
@login_required
def admin():
    return redirect(url_for(admin))


@app.route("/inputs")
@login_required
def data():
    db.create_all()
    try:
        all_data = UserData.query.filter_by(user_id=current_user.id).all()
    except:
        all_data = []
    return render_template("inputs.html", all_data=all_data, datetime=datetime)


@app.route("/new_data", methods=["GET", "POST"])
@login_required
def new_data():
    db.create_all()
    form = forms.DataForm()
    if form.validate_on_submit():
        new_data_value = UserData(income=form.income.data, amount=form.amount.data, user_id=current_user.id)
        db.session.add(new_data_value)
        db.session.commit()
        flash(f"Įrašas sukurtas", 'success')
        return redirect(url_for('data'))
    return render_template("add_data.html", form=form)


@app.route("/delete/<int:id>")
@login_required
def delete(id):
    user_data = UserData.query.get(id)
    db.session.delete(user_data)
    db.session.commit()
    return redirect(url_for('data'))


@app.route("/update/<int:id>", methods=['GET', 'POST'])
@login_required
def update(id):
    form = forms.DataForm()
    user_data = UserData.query.get(id)
    if form.validate_on_submit():
        user_data.income = form.income.data
        user_data.amount = form.amount.data
        db.session.commit()
        return redirect(url_for('data'))
    return render_template("update.html", form=form, user_data=user_data)


@app.route("/balance")
@login_required
def balance():
    try:
        all_data = UserData.query.filter_by(user_id=current_user.id)
    except:
        all_data = []
    user_balance = 0
    for user_data in all_data:
        if user_data.income:
            user_balance += user_data.amount
        else:
            user_balance -= user_data.amount
    return render_template("balance.html", balance=user_balance)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    db.create_all()