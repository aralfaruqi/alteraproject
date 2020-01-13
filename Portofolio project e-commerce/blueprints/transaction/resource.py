from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from sqlalchemy import desc
from .model import Transactions
from blueprints.product.model import Products
from blueprints.client.model import Clients
from blueprints.transaction_details.model import Transaction_detailss
from blueprints import db,app, internal_required, pembeli_required
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_transaction = Blueprint('transaction', __name__)
api = Api(bp_transaction)

class TransactionList(Resource):
    def __init__(self):
        pass

    #Get all transaction
    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('pembeli_id', type=int, location='args')

        args = parser.parse_args()

        offset = (args['p']*args['rp'])-args['rp']

        qry_transaction = Transactions.query

        if args['pembeli_id'] is not None:
            qry_transaction = qry_transaction.filter_by(pembeli_id=args['pembeli_id'])

        rows = []
        for row in qry_transaction.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Transactions.response_fields))
        
        return rows, 200
        
class TransactionResource(Resource):
    def __init__(self):
        pass

    #Buat transaction baru untuk setiap calon pembeli
    @jwt_required
    @pembeli_required
    def post(self):
        claim = get_jwt_claims()
        qry_transaction = Transactions.query.filter_by(status='process').filter_by(pembeli_id=claim['id']).first()

        if qry_transaction is None :
            transaction = Transactions(claim['id'],"Bank BCA",0,0,0,0,'process')
            db.session.add(transaction)
            db.session.commit()

            app.logger.debug('DEBUG : %s', transaction)

            return marshal(transaction, Transactions.response_fields), 200, {'Content-Type':'application/json'}
        return {'message':'cart sudah dibuat'}

    #Update status transaction dan transaction_details setiap pembeli klik buat pesanan
    @jwt_required
    @pembeli_required
    def put(self):
        claim = get_jwt_claims()
        qry_transaction = Transactions.query.filter_by(status='process').filter_by(pembeli_id=claim['id']).first()

        parser = reqparse.RequestParser()
        parser.add_argument('metode_pembayaran', location='json')

        args = parser.parse_args()
        qry_transaction.metode_pembayaran = args["metode_pembayaran"]

        if qry_transaction is not None :
            qry_transaction_details = Transaction_detailss.query.filter_by(transaction_id=qry_transaction.id)
            for qry in qry_transaction_details :
                qry_transaction.harga_barang_total += qry.harga
                qry_transaction.biaya_ongkir_total += qry.biaya_ongkir
                qry_transaction.total_barang +=1
                qry.status = 'terpesan'

            qry_transaction.total_harga = qry_transaction.harga_barang_total+qry_transaction.biaya_ongkir_total 
            qry_transaction.status = 'order terkirim'

            db.session.commit()

            return marshal(qry_transaction, Transactions.response_fields), 200, {'Content-Type':'application/json'}

        return {'status' : 'UNAUTHORIZED'}

api.add_resource(TransactionList,'/admin')
api.add_resource(TransactionResource, '/pembeli')
