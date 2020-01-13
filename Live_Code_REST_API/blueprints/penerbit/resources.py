from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from sqlalchemy import desc
from datetime import datetime
from .model import Penerbits
from blueprints import db, app

bp_penerbit = Blueprint('penerbit', __name__)
api = Api(bp_penerbit)

class PenerbitResource(Resource):
    def __init__(self):
        pass

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('isbn', location='json', required=True)
        parser.add_argument('title', location='json', required=True)
        parser.add_argument('nama_penerbit', location='json', required=True)
        parser.add_argument('harga', type=int, location='json', required=True)
        parser.add_argument('buku_id', type=int, location='json')

        args = parser.parse_args()

        penerbit = Penerbits(args['isbn'], args['title'], args['nama_penerbit'], args['harga'], args['buku_id'] )
        marshalPenerbit = marshal(penerbit, Penerbits.response_fields)
        query_buku = Bukus.query.get(marshalPenerbit['buku_id'])
        marshalBuku = marshal(query_buku, Bukus.response_fields)

        marshalPenerbit['data'] = marshalBuku

        db.session.add(penerbit)
        db.session.commit()

        app.logger.debug('DEBUG : %s', penerbit)

        return marshal(penerbit, Penerbits.response_fields), 200, {'Content-Type' : 'application/json'}

class Public(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, location='args', default=1)
        parser.add_argument('per_page', type=int, location='args', default=25)
        parser.add_argument('id', type=int, location='args')
        parser.add_argument('isbn', type=int, location='args')
        parser.add_argument('status', location='args', help='invalid status', choices=('show', 'not_show')
        parser.add_argument('orderby', location='args', help='invalid orderby value', choices=('isbn', 'id', 'status'))
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc', 'asc'))
        args = parser.parse_args()

        offset = (args['page'] * args['per_page']) - args['per_page']

        qry = Bukus.query

        if args['id'] is not None:
            qry = qry.filter_by(id=args['id'])
        
        if args['isbn'] is not None:
            qry = qry.filter_by(isbn=args['isbn'])

        if args['status'] is not None:
            qry = qry.filter_by(status=args['status'])

        if args['orderby'] is not None:
            if args['orderby'] == 'isbn':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Bukus.isbn))
                else:
                    qry = qry.order_by(Bukus.isbn)
            elif args['orderby'] == 'id':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Bukus.id))
                else:
                    qry = qry.order_by(Bukus.id)
            elif args['orderby'] == 'status':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Bukus.status))
                else:
                    qry = qry.order_by(Bukus.status)

        rows = []
        for row in qry.limit(args['per_page']).offset(offset).all():
            rows.append(marshal(row, Bukus.response_fields))

        return rows, 200

class PenerbitList(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('nama_penerbit', location='args')
        parser.add_argument('orderby', location='args', help='invalid order by value', choices=('client_key', 'client_secret', 'id'))
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc', 'asc'))

        args = parser.parse_args()

        offset = (args['p']*args['rp'] - args['rp'])

        # qry = Clients.query.filter(Clients.name.like("%"+args['name']+"%"))

        qry = Penerbits.query

        if args['status'] is not None :
            qry = qry.filter_by(status=args['status'])

        if args['orderby'] is not None :
            if args['orderby'] == 'client_key':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Penerbits.client_key))
                else:
                    qry = qry.order_by(Penerbits.client_key)
            
            elif args['orderby'] == 'client_secret' :
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Penerbits.client_secret))
                else:
                    qry = qry.order_by(Penerbits.client_secret)

            elif args['orderby'] == 'id' :
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Penerbits.id))
                else:
                    qry = qry.order_by(Penerbits.id)
                

        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Penerbits.response_fields))
        
        return rows, 200

api.add_resource(PenerbitList, '', '/list')
api.add_resource(PenerbitResource, '', '/<id>')
api.add_resource(Public, '', '/list')
