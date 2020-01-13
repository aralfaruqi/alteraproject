from blueprints import db
from flask_restful import fields

class Bukus(db.Model):
	__tablename__ = "buku"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	isbn = db.Column(db.String(30), unique=True, nullable=False, required=True)
	title = db.Column(db.String(30), nullable=False, required=True)
	pengarang = db.Column(db.String(10), nullable=False)
	penerbit = db.Column(db.String(10), nullable=False, required=True)
	harga = db.Column(db.Integer, nullable=False)
	status = db.Column(db.String(10), nullable=False)
	client_id = db.Column(db.Integer, db.ForeignKey("client.id" ,ondelete='CASCADE'))

	response_fields = {
		'id': fields.Integer,
		'isbn': fields.String,
		'title': fields.String,
		'pengarang': fields.String,
		'penerbit': fields.String,
		'harga': fields.Integer,
		'status': fields.String,
		'client_id': fields.Integer
	}

	def __init__(self, isbn, title, pengarang, penerbit, harga, status, client_id):
		self.isbn = isbn
		self.title = title
		self.pengarang = pengarang
		self.penerbit = penerbit
		self.harga = harga
		self.pengarang = pengarang
		self.pengarang = pengarang

	def __repr__(self):
		return '<Buku %r>' % self.title
