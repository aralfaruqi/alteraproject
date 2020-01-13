from blueprints import db
from flask_restful import fields
import datetime

class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(255), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id", ondelete='CASCADE'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now(), default=datetime.datetime.now())
    deleted = db.Column(db.Boolean, default=False)
   
    response_fields = {
        'created_at' : fields.DateTime,
        'updated_at' : fields.DateTime,
        'deleted' : fields.Boolean,
        'id' : fields.Integer,
        'name' : fields.String,
        'age' : fields.Integer,
        'sex' : fields.String,
        'client_id' : fields.Integer
    }

    def __init__(self, name, age, sex, client_id):
        self.name = name
        self.age = age
        self.sex = sex
        self.client_id = client_id

    def __repr__(self):
        return '<User %r>' %self.id