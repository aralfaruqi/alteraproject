from blueprints import db
from flask_restful import fields
import datetime

class Transactions(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pembeli_id = db.Column(db.Integer, db.ForeignKey("client.id", ondelete='CASCADE'), nullable=False)
    metode_pembayaran = db.Column(db.String(255), default="Bank BCA")
    harga_barang_total = db.Column(db.Integer, default=0)
    biaya_ongkir_total = db.Column(db.Integer, default = 0)
    total_harga = db.Column(db.Integer, default = 0)
    total_barang = db.Column(db.Integer, default=0)
    status = db.Column(db.String(255), default='process')
    waktu_diproses = db.Column(db.DateTime, default=datetime.datetime.now())
    waktu_dikirim = db.Column(db.DateTime, onupdate=datetime.datetime.now(), default=datetime.datetime.now())

    response_fields = {
        'id' : fields.Integer,
        'pembeli_id' : fields.Integer,
        'metode_pembayaran' : fields.String,
        'harga_barang_total' : fields.Integer,
        'biaya_ongkir_total' : fields.Integer,
        'total_harga' : fields.Integer,
        'total_barang' : fields.Integer,
        'status' : fields.String,
        'waktu_diproses' : fields.DateTime,
        'waktu_dikirim' : fields.DateTime
    }

    def __init__(self, pembeli_id, metode_pembayaran, harga_barang_total, biaya_ongkir_total, total_harga, total_barang, status):
        self.pembeli_id =pembeli_id
        self.metode_pembayaran = metode_pembayaran
        self.harga_barang_total = harga_barang_total
        self.biaya_ongkir_total = biaya_ongkir_total
        self.total_harga = total_harga
        self.total_barang = total_barang
        self.status = status
        
    def __repr__(self):
        return '<transaction %r>' %self.id