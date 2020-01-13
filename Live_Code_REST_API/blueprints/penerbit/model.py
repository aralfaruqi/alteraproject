from blueprints import db
from flask_restful import fields


class Penerbits(db.Model):
	__tablename__ = "penerbit"
	client_key = db.Column(db.String(30), primary_key=True)
	client_secret = db.Column(db.String(30), nullable=False)
	nama_penerbit = db.Column(db.String(30), nullable=False, required=True)
	buku_id = db.Column(db.Integer, db.ForeignKey("buku.id" ,ondelete='CASCADE'))
	isbn = db.Column(db.String(30), db.ForeignKey("buku.isbn" ,ondelete='CASCADE'))
	title = db.Column(db.String(30), db.ForeignKey("buku.title" ,ondelete='CASCADE'))
	harga = db.Column(db.Integer, db.ForeignKey("buku.harga" ,ondelete='CASCADE'))

	response_fields = {
		'client_key': fields.String,
		'client_secret': fields.String,
		'nama_penerbit': fields.String,
		'buku_id' : fields.Integer,
		'isbn' : fields.String,
		'title' : fields.String,
		'harga' : fields.Integer
	}

	jwt_claims_fields = {
		'client_key': fields.String,
		'client_secret': fields.String,
		'nama_penerbit': fields.String,
		'buku_id' : fields.Integer,
		'isbn' : fields.String,
		'title' : fields.String,
		'harga' : fields.Integer
	}

	def __init__(self, isbn, title, nama_penerbit, harga, buku_id):
		self.isbn = isbn
		self.title = title
		self.nama_penerbit = nama_penerbit
		self.harga = harga
		self.buku_id = buku_id

	def __repr__(self):
		return '<Penerbit %r>' % self.title
