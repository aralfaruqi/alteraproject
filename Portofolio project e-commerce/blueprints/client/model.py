from blueprints import db
from flask_restful import fields
import datetime

class Clients(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(255), nullable=False)
    no_telepon = db.Column(db.String(255), nullable=False)
    no_rekening = db.Column(db.String(255), nullable=False)
    lokasi = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    jenis_akun = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    update_at = db.Column(db.DateTime, onupdate=datetime.datetime.now(), default=datetime.datetime.now())

    response_fields = {
        'id' : fields.Integer,
        'nama' : fields.String,
        'no_telepon' : fields.Integer,
        'no_rekening' : fields.String,
        'lokasi' : fields.String,
        'email' : fields.String,
        'password' : fields.String,
        'jenis_akun' : fields.String,
        'created_at' : fields.DateTime,
        'updated_at' : fields.DateTime
    }

    jwt_claims_fields = {
        'id' : fields.Integer,
        'email' : fields.String,
        'password' : fields.String,
        'jenis_akun' : fields.String
    }

    def __init__(self, nama, no_telepon, no_rekening, lokasi, email, password, jenis_akun):
        self.nama = nama
        self.no_telepon = no_telepon
        self.no_rekening = no_rekening
        self.lokasi = lokasi
        self.email = email
        self.password = password
        self.jenis_akun = jenis_akun

    def __repr__(self):
        return '<Client %r>' %self.id