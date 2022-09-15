import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import forms

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'saskaitos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column("Vardas", db.String)
    lname = db.Column("Pavardė", db.String)
    code = db.Column("Asmens kodas", db.Integer)
    phone = db.Column("Telefonas", db.Integer)
    account = db.relationship("Accounts", back_populates="person")


class Banks(db.Model):
    __tablename__ = "bank"
    id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column("Pavadinimas", db.String)
    adress = db.Column("Adresas", db.String)
    bank_code = db.Column("Banko kodas", db.Integer)
    swift_code = db.Column("SWIFT kodas", db.Integer)
    account = db.relationship("Accounts", back_populates="bank")


class Accounts(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    acc_number = db.Column("Saskaita", db.Integer)
    balance = db.Column("Balansas", db.Integer)
    bank_id = db.Column(db.Integer, db.ForeignKey("bank.id"))
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    bank = db.relationship("Banks", back_populates="account")
    person = db.relationship("Person", back_populates="account")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/person")
def people():
    try:
        all_people = Person.query.all()
    except:
        all_people = []
    return render_template("person.html", all_people=all_people)


@app.route("/banks")
def bank():
    try:
        all_banks = Banks.query.all()
    except:
        all_banks = []
    return render_template("banks.html", all_banks=all_banks)


@app.route("/account")
def accounts():
    try:
        all_accounts = Accounts.query.all()
    except:
        all_accounts = []
    return render_template("accounts.html", all_accounts=all_accounts)


@app.route("/add_person", methods=["GET", "POST"])
def add_person():
    db.create_all()
    form = forms.PersonForm()
    if form.validate_on_submit():
        new_person = Person(fname=form.fname.data, lname=form.lname.data, code=form.code.data, phone=form.phone.data)
        db.session.add(new_person)
        db.session.commit()
        return redirect(url_for('people'))
    return render_template("add_person.html", form=form)


@app.route("/new_bank", methods=["GET", "POST"])
def add_bank():
    db.create_all()
    form = forms.BanksForm()
    if form.validate_on_submit():
        new_bank = Banks(bank_name=form.bank_name.data, adress=form.adress.data, bank_code=form.bank_code.data, swift_code=form.swift_code.data)
        db.session.add(new_bank)
        db.session.commit()
        return redirect(url_for('bank'))
    return render_template("new_bank.html", form=form)


@app.route("/new_account", methods=["GET", "POST"])
def add_account():
    db.create_all()
    form = forms.AccountsForm()
    if form.validate_on_submit():
        new_account = Accounts(acc_number=form.acc_number.data, balance=form.balance.data, bank_id=form.bank.data.id, person_id=form.person.data.id)
        db.session.add(new_account)
        db.session.commit()
        return redirect(url_for('accounts'))
    return render_template("new_account.html", form=form)


@app.route("/delete/<int:id>")
def delete(id):
    get_id = Person.query.get(id)
    db.session.delete(get_id)
    db.session.commit()
    return redirect(url_for('people'))


@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    form = forms.PersonForm()
    person = Person.query.get(id)
    if form.validate_on_submit():
        person.fname = form.fname.data
        person.lname = form.lname.data
        person.code = form.code.data
        person.phone = form.phone.data
        db.session.commit()
        return redirect(url_for('people'))
    return render_template("update.html", form=form, person=person)


@app.route("/bank_delete/<int:id>")
def bank_delete(id):
    get_id = Banks.query.get(id)
    db.session.delete(get_id)
    db.session.commit()
    return redirect(url_for('bank'))


@app.route("/bank_update/<int:id>", methods=['GET', 'POST'])
def bank_update(id):
    form = forms.BanksForm()
    bank = Banks.query.get(id)
    if form.validate_on_submit():
        bank.bank_name = form.bank_name.data
        bank.adress = form.adress.data
        bank.bank_code = form.bank_code.data
        bank.swift_code = form.swift_code.data
        db.session.commit()
        return redirect(url_for('bank'))
    return render_template("bank_update.html", form=form, bank=bank)


@app.route("/account_delete/<int:id>")
def account_delete(id):
    get_id = Accounts.query.get(id)
    db.session.delete(get_id)
    db.session.commit()
    return redirect(url_for('accounts'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    db.create_all()
