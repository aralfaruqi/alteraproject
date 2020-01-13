from blueprints import db
from flask_restful import fields
import datetime

class Books(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    category = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now(), default=datetime.datetime.now())
    deleted = db.Column(db.Boolean, default=False)

    response_fields = {
        'created_at' : fields.DateTime,
        'updated_at' : fields.DateTime,
        'deleted' : fields.Boolean,
        'id' : fields.Integer,
        'title' : fields.String,
        'category' : fields.String,
        'author' : fields.String
    }

    def __init__(self, title, category, author):
        self.title = title
        self.category = category
        self.author = author

    def __repr__(self):
        return '<Book %r>' %self.id