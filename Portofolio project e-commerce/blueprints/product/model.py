from blueprints import db
from flask_restful import fields

class Products(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_produk = db.Column(db.String(255), nullable=False)
    kategori = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    lokasi_kota = db.Column(db.String(255), nullable=False)
    harga_awal = db.Column(db.Integer)
    persen_discount = db.Column(db.Integer)
    deskirpsi_produk = db.Column(db.String(1000), nullable=False)
    gratis_ongkir = db.Column(db.Boolean, default=False)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id", ondelete='CASCADE'), nullable=False)
    nama_supplier = db.Column(db.String(255), nullable=False)


    response_fields = {
        'id' : fields.Integer,
        'nama_produk' : fields.String,
        'kategori' : fields.String,
        'brand' : fields.String,
        'harga' : fields.Integer,
        'lokasi_kota' : fields.String,
        'harga_awal' : fields.Integer,
        'persen_discount' : fields.Integer,
        'deskirpsi_produk' : fields.String,
        'gratis_ongkir' : fields.Boolean,
        'client_id' : fields.Integer,
        'nama_supplier' : fields.String
    }

    def __init__(self, nama_produk, kategori, brand, harga, lokasi_kota, harga_awal, persen_discount, deskirpsi_produk, gratis_ongkir, client_id, nama_supplier):
        self.nama_produk = nama_produk
        self.kategori = kategori
        self.brand = brand
        self.harga = harga
        self.lokasi_kota = lokasi_kota
        self.harga_awal = harga_awal
        self.persen_discount = persen_discount
        self.deskirpsi_produk = deskirpsi_produk
        self.gratis_ongkir = gratis_ongkir
        self.client_id = client_id
        self.nama_supplier = nama_supplier

    def __repr__(self):
        return '<Product %r>' %self.id