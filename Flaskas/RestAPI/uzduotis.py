from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_marshmallow import Marshmallow
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'to_do.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


# DB objektas
class Uzduotis(db.Model):
    __tablename__ = 'uzduotis'
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column("Pavadinimas", db.String)
    atlikta = db.Column("Atlikta", db.Boolean)


# Užduoties schema
class UzduotisSchema(ma.Schema):
    class Meta:
        fields = ('id', 'pavadinimas', 'atlikta')


uzduotis_schema = UzduotisSchema()
uzduotys_schema = UzduotisSchema(many=True)


# Crud
class PridetiUzduoti(Resource):
    def post(self):
        db.create_all()
        try:
            pavadinimas = request.json['pavadinimas']
            atlikta = request.json['atlikta']
            nauja_uzduotis = Uzduotis(pavadinimas=pavadinimas, atlikta=atlikta)
            db.session.add(nauja_uzduotis)
            db.session.commit()
        except Exception as e:
            return 'Bad requests', 400
        return uzduotis_schema.dump(nauja_uzduotis), 201

    def get(self, id=None):
        if id:
            uzduotis = Uzduotis.query.get_or_404(id)
            return uzduotis_schema.dump(uzduotis)
        else:
            visos_uzduotys = Uzduotis.query.all()
            return uzduotys_schema.dump(visos_uzduotys), 201

    def delete(self, id):
        uzduotis = Uzduotis.query.get_or_404(id)
        db.session.delete(uzduotis)
        db.session.commit()
        return '', 204

    def put(self, id):
        uzduotis = Uzduotis.query.get_or_404(id)
        uzduotis.pavadinimas = request.json['pavadinimas']
        uzduotis.atlikta = request.json['atlikta']
        db.session.commit()
        return uzduotis_schema.dump(uzduotis), 201


api.add_resource(PridetiUzduoti, '/uzduotis', '/uzduotis/<int:id>')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    db.create_all()
