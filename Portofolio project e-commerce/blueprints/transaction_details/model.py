from blueprints import db
from flask_restful import fields
import datetime

class Transaction_detailss(db.Model):
    __tablename__ = 'transaction_details'

    transaction_id = db.Column(db.Integer, db.ForeignKey("transaction.id", ondelete='CASCADE'), nullable=False, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id", ondelete='CASCADE'), nullable=False, primary_key=True)
    supplier_id = db.Column(db.Integer, nullable=False)
    nama_supplier = db.Column(db.String(255), nullable=False)
    kuantitas = db.Column(db.Integer, nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    metode_pengiriman = db.Column(db.String(255), nullable=False)
    biaya_ongkir = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False, default='process')

    response_fields = {
        'transaction_id' : fields.Integer,
        'product_id' : fields.Integer,
        'supplier_id' : fields.Integer,
        'nama_supplier' : fields.String,
        'kuantitas' : fields.Integer,
        'harga' : fields.Integer,
        'metode_pengiriman' : fields.String,
        'biaya_ongkir' : fields.Integer,
        'status' : fields.String
    }

    def __init__(self, transaction_id, product_id, supplier_id, nama_supplier, kuantitas, harga, metode_pengiriman, biaya_ongkir, status):
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.supplier_id = supplier_id
        self.nama_supplier = nama_supplier
        self.kuantitas = kuantitas
        self.harga = harga
        self.metode_pengiriman = metode_pengiriman
        self.biaya_ongkir = biaya_ongkir
        self.status = status
        
    def __repr__(self):
        return '<transaction_details %r>' %self.transaction_id