from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.String)

    #animals = db.relationship('Animal', backref='animals')

    #def __init__(self, name, birthday):
    #    self.name = name
    #    self.birthday = birthday
        
class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    #animals = db.relationship('Animal', backref='enclosers')

    #def __init__(self, environment, open_to_visitors):
    #   self.environment = environment
    #    self.open_to_visitors = open_to_visitors

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    #zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    #enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    #zookeeper = db.relationship('Zookeeper', backref='animals')
    #enclosure = db.relationship('Enclosure', backref='animals')

    #def __init__(self, name, species):
    #    self.name = name
    #    self.species = species
