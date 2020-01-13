from blueprints import db
from flask_restful import fields
import datetime

class Books(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), nullable=False)
    isbn = db.Column(db.String(30), nullable=False)
    writer = db.Column(db.String(30), nullable=False)
    deleted = db.Column(db.Boolean, default = False)
    created_at = db.Column(db.DateTime, default = datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default = datetime.datetime.now(), onupdate = datetime.datetime.now())

    response_fields = {
        'id' : fields.Integer,
        'title' : fields.String,
        'isbn' : fields.String,
        'writer' : fields.String,
        'deleted' : fields.Boolean,
        'created_at' : fields.DateTime,
        'updated_at' : fields.DateTime,
    }

    def __init__(self, title, isbn, writer):
        self.title = title
        self.isbn = isbn
        self.writer = writer

    def __repr__(self):
        return '<Book %r>' % self.id