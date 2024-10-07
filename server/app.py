#!/usr/bin/env pyt
from flask import Flask,jsonify ,request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Hero, Power, HeroPower
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
app = Flask(__name__)
@app.route('/heroes',methods=['GET'])
def get_heroes():
  heroes = Hero.query.all()
  return jsonify ([hero.name for hero in heroes]),200

@app.route('/heroes/:id',methods=[' POST'])
def create_hero():
   data = request.get_json
   new_hero =Hero(name=data['name']),superpower = data['superpower']
   db.session.add(new_hero)
   db.session.commit()
   return jsonify({"message":"hero created!}),201
if __name__ == '__main__':
    app.run(port=5555, debug=True)
sk(__namapp = Flae__)