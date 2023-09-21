#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()
    response_body = f'''
        <ul>Name: {animal.name}</ul>
        <ul>Species: {animal.species}</ul>
        <ul>Zookeeper: {animal.zookeeper}</ul>
        <ul>Enclosure: {animal.enclosure}</ul>
    '''
    response = make_response(response_body, 200)
    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    keeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    animals = []
    for animal in Animal.query.filter(Animal.zookeeper_id == id).all():
        animals.append(animal.name)
    response_body = f'''
        <ul>Name: {keeper.name}</ul>
        <ul>Birthday: {keeper.birthday}</ul>
    '''
    for animal in animals:
        response_body += f'<ul>Animal: {animal}</ul>'
    response = make_response(response_body, 200)

    return response

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    animals = []
    for animal in Animal.query.filter(Animal.enclosure_id == id).all():
        animals.append(animal.name)
    response_body =f"""
        <ul>Environment: {enclosure.environment}</ul>
        <ul>Open to Visitors: {enclosure.open_to_visitors}</ul>
    """
    for animal in animals:
        response_body += f'<ul>Animal: {animal}</ul>'
    response = make_response(response_body, 200)
    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
