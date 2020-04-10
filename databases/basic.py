import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # pip install Flask-Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> C://User/SomeUser/Projects/basic.py // it works on every OS
print(basedir)


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

class Pokemon(db.Model):

    # MANUAL TABLE NAME CHOICE
    __tablename__ = 'pokemons'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    level = db.Column(db.Integer)
    type = db.Column(db.Text)

    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type

    def __repr__(self):
        return f"Pokemon {self.name} is level {self.level} and {self.type} type."
