from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from sqlalchemy import desc
from .model import Transaction_detailss
from blueprints.product.model import Products
from blueprints.client.model import Clients
from blueprints.transaction.model import Transactions
from blueprints import db,app, internal_required, pembeli_required, supplier_required
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_transaction_details = Blueprint('transaction_details', __name__)
api = Api(bp_transaction_details)

class Transaction_detailsList(Resource):
    def __init__(self):
        pass

    #Get all transaction details (product apa saja yang dibeli)
    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('product_id', type=int, location='args')
        parser.add_argument('supplier_id', type=int, location='args')

        args = parser.parse_args()

        offset = (args['p']*args['rp'])-args['rp']

        qry_transaction_details = Transaction_detailss.query

        if args['product_id'] is not None:
            qry_transaction_details = qry_transaction_details.filter_by(product_id=args['product_id'])

        if args['supplier_id'] is not None:
            qry_transaction_details = qry_transaction_details.filter_by(supplier_id=args['supplier_id'])

        rows = []
        for row in qry_transaction_details.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Transaction_detailss.response_fields))
        
        return rows, 200
        
class TambahKeCartResource(Resource):
    def __init__(self):
        pass

    #tambah product yang akan dibeli pembeli ke cart 
    @jwt_required
    @pembeli_required
    def post(self):
        claim = get_jwt_claims()
        qry_transaction = Transactions.query.filter_by(status='process').filter_by(pembeli_id=claim['id']).first()

        parser = reqparse.RequestParser()
        parser.add_argument('product_id', type=int, location='json', required=True)
        parser.add_argument('supplier_id', type=int, location='json', required=True)
        parser.add_argument('nama_supplier', location='json', required=True)
        parser.add_argument('kuantitas', type=int, location='json', required=True)
        parser.add_argument('harga', type=int, location='json', required=True)
        parser.add_argument('metode_pengiriman', location='json', required=True)
        
        args = parser.parse_args()
        
        if qry_transaction is not None :
            if args['metode_pengiriman'] == 'Fast Delivery 24 Jam' :
                self.biaya_ongkir = 30000
            else :
                self.biaya_ongkir = 10000

            Transaction_details = Transaction_detailss(qry_transaction.id, args['product_id'], args['supplier_id'], args['nama_supplier'], args['kuantitas'], args['harga'], args['metode_pengiriman'], self.biaya_ongkir, 'process') 
            db.session.add(Transaction_details)
            db.session.commit()

            app.logger.debug('DEBUG : %s', Transaction_details)

            return marshal(Transaction_details, Transaction_detailss.response_fields), 200, {'Content-Type':'application/json'}
        return {'status' : 'UNAUTHORIZED'}

class KirimPesananResource(Resource):
    #Pesanan yang masuk ke halaman supplier, ketika di klik kirim pesanan maka status terpesan menjadi terkirim
    @jwt_required
    @supplier_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_id', type=int, location='json', required=True)

        args = parser.parse_args()

        claim = get_jwt_claims()

        qry_transaction_details = Transaction_detailss.query.filter_by(status='terpesan').filter_by(product_id=args['product_id']).filter_by(supplier_id=claim['id']).first()

        if qry_transaction_details is not None :
            qry_transaction_details.status = 'terkirim'

            db.session.commit()

            return marshal(qry_transaction_details, Transaction_detailss.response_fields), 200, {'Content-Type':'application/json'}
        return {'status' : 'UNAUTHORIZED'}

api.add_resource(Transaction_detailsList,'/admin')
api.add_resource(TambahKeCartResource, '/pembeli')
api.add_resource(KirimPesananResource, '/supplier')
