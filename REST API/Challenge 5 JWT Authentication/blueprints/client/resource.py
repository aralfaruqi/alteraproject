import hashlib, datetime
from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from sqlalchemy import desc
from .model import Clients
from blueprints import db,app, internal_required
from flask_jwt_extended import jwt_required
from password_strength import PasswordPolicy

bp_client = Blueprint('client', __name__)
api = Api(bp_client)

class ClientList(Resource):
    def __init__(self):
        pass

    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('status', location='args')
        parser.add_argument('orderby', location='args', help='invalid order value', choices=('client_key', 'id', 'client_secret'))
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc','asc'))

        args = parser.parse_args()

        offset = (args['p']*args['rp'])-args['rp']

        qry = Clients.query

        if args['status'] is not None:
            qry = qry.filter_by(status=args['status'])

        if args['orderby'] is not None:
            if args['orderby'] =='id':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Clients.id))
                else:
                    qry = qry.order_by(Clients.id)
            elif args['orderby'] =='client_key':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Clients.client_key))
                else:
                    qry = qry.order_by(Clients.client_key)
            elif args['orderby'] =='client_secret':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Clients.client_secret))
                else:
                    qry = qry.order_by(Clients.client_secret)

        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Clients.response_fields))
        
        return rows, 200

class ClientResource(Resource):
    def __init__(self):
        pass
    
    @jwt_required
    @internal_required
    def get(self, id):
        qry = Clients.query.get(id)
        if qry is not None:
            return marshal(qry, Clients.response_fields), 200
        return {'status': 'NOT_FOUND'}, 404

    @jwt_required
    @internal_required
    def post(self):
        policy = PasswordPolicy.from_names(
            length = 6,
            numbers = 1
        )

        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='json', required=True)
        parser.add_argument('client_secret', location='json', required=True)
        parser.add_argument('status', location='json', required=True)

        args = parser.parse_args()

        validation = policy.test(args['client_secret'])

        if validation == []:
            password_digest = hashlib.md5(args['client_secret'].encode()).hexdigest()
            client = Clients(args['client_key'], password_digest, args['status'])

            db.session.add(client)
            db.session.commit()

            app.logger.debug('DEBUG : %s', client)

            return marshal(client, Clients.response_fields), 200, {'Content-Type':'application/json'}
    
    @jwt_required
    @internal_required
    def put(self, id):
        policy = PasswordPolicy.from_names(
            length = 6,
            numbers = 1
        )

        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='json', required=True)
        parser.add_argument('client_secret', location='json', required=True)
        parser.add_argument('status', location='json', required=True)

        args = parser.parse_args()

        validation = policy.test(args['client_secret'])

        if validation == []:
            password_digest = hashlib.md5(args['client_secret'].encode()).hexdigest()
            qry = Clients.query.get(id)

            if qry is None:
                return {'status': 'NOT_FOUND'}, 404
            
            qry.client_key = args['client_key']
            qry.client_secret = password_digest
            qry.status = args['status']

            db.session.commit()

            return marshal(qry, Clients.response_fields), 200, {'Content-Type':'application/json'}
    
    @jwt_required
    @internal_required
    def delete(self, id):
        qry = Clients.query.get(id)
        if qry is None:
            return {'status' : 'NOT_FOUND'}, 404
        
        db.session.delete(qry)
        db.session.commit()

api.add_resource(ClientList, '','/list')
api.add_resource(ClientResource, '','/<id>')


