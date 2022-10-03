import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite?check_same_thread=False')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

association_table = db.Table('association', db.metadata,
    db.Column('tevas_id', db.Integer, db.ForeignKey('tevas.id')),
    db.Column('vaikas_id', db.Integer, db.ForeignKey('vaikas.id'))
)


class Students(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column("Vardas", db.String)
    lname = db.Column("Pavardė", db.String)
    courses = db.relationship("Vaikas", secondary=association_table, back_populates="tevai")


class Teachers(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)
    courses = db.relationship("Tevas", secondary=association_table, back_populates="vaikai")