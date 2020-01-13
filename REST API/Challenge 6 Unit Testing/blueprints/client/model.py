from blueprints import db
from flask_restful import fields
import datetime

class Clients(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_key = db.Column(db.String(255), unique=True, nullable=False)
    client_secret = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now(), default=datetime.datetime.now())
    deleted = db.Column(db.Boolean, default=False)

    response_fields = {
        'created_at' : fields.DateTime,
        'updated_at' : fields.DateTime,
        'deleted' : fields.String,
        'id' : fields.Integer,
        'client_key' : fields.String,
        'client_secret' : fields.String,
        'status' : fields.String
    }

    jwt_claims_fields = {
        'client_key' : fields.String,
        'status' : fields.String
    }

    def __init__(self, client_key, client_secret, status):
        self.client_key = client_key
        self.client_secret = client_secret
        self.status = status

    def __repr__(self):
        return '<Client %r>' %self.id