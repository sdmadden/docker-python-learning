from db import db
from constants import fruit as FRUIT

import json

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    fruit = db.Column(db.SmallInteger, default=FRUIT.ORANGE)

    def __init__(self, name=None, fruit=None):
        self.name = name
        self.fruit = fruit

    def get_fruit(self):
        return FRUIT.TYPES[self.fruit]

    def __repr__(self):
        return f'<User {self.name} {self.get_fruit()}>'

    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "fruit": self.get_fruit()
        }
