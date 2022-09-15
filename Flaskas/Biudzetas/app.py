from flask import Flask, redirect, render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from form import Budget
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'bet kokia simbolių eilutė'


app.config.update(TEMPLATES_AUTO_RELOAD=True)
db = SQLAlchemy(app)


class Budget2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Integer(), nullable=False)
    type = db.Column(db.String())
    date_created = db.Column(db.DateTime)


db.create_all()


@app.route('/', methods=['POST', 'GET'])
def index():
    form = Budget()
    if form.validate_on_submit():
        income = form.income.data
        type = form.type.data
        new_income = Budget2(income=income, type=type, date_created=datetime.now().replace(microsecond=0))
        try:
            db.session.add(new_income)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as ex:
            return ex
    else:
        budget = Budget2.query.all()
        return render_template('index.html', budget=budget, form=form)


@app.route('/balance', methods=['POST', 'GET'])
def balance():
    budget = Budget2.query.all()
    income = 0
    expenses = 0
    for item in budget:
        if item.type == 'Pajamos':
            income += item.income
        else:
            expenses += item.income
    value = income - expenses
    return render_template('balance.html', value=value)


if __name__ == "__main__":
    app.run(debug=True)
