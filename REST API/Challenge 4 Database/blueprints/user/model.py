from blueprints import db
from flask_restful import fields
import datetime

class Users(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id", ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(30), unique=True, nullable=False)
    age = db.Column(db.String(30), nullable=False)
    sex = db.Column(db.String(30), nullable=False)
    deleted = db.Column(db.Boolean, default = False)
    created_at = db.Column(db.DateTime, default = datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default = datetime.datetime.now(), onupdate = datetime.datetime.now())

    response_fields = {
        'id' : fields.Integer,
        'client_id' : fields.Integer,
        'name' : fields.String,
        'age' : fields.String,
        'sex' : fields.String,
        'deleted' : fields.Boolean,
        'created_at' : fields.DateTime,
        'updated_at' : fields.DateTime
    }

    def __init__(self, client_id, name, age, sex):
        self.client_id = client_id
        self.name = name
        self.age = age
        self.sex = sex

    def __repr__(self):
        return '<User %r>' % self.id