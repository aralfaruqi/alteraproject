import hashlib, datetime
from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from sqlalchemy import desc
from .model import Clients
from blueprints import db,app, internal_required
from flask_jwt_extended import jwt_required, get_jwt_claims
from password_strength import PasswordPolicy

bp_client = Blueprint('client', __name__)
api = Api(bp_client)

class ClientList(Resource):
    def __init__(self):
        pass

    #Get all client (pembeli dan supplier)
    @jwt_required
    @internal_required # Admin only
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('orderby', location='args', help='invalid order value', choices=('created_at', 'id'))
        parser.add_argument('jenis_akun', location='args')
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc','asc'))

        args = parser.parse_args()

        offset = (args['p']*args['rp'])-args['rp']

        qry = Clients.query

        if args['jenis_akun'] is not None:
            qry = qry.filter_by(jenis_akun=args['jenis_akun'])

        if args['orderby'] is not None:
            if args['orderby'] =='id':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Clients.id))
                else:
                    qry = qry.order_by(Clients.id)
            elif args['orderby'] =='created_at':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Clients.created_at))
                else:
                    qry = qry.order_by(Clients.created_at)

        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Clients.response_fields))
        
        return rows, 200

class ClientResource(Resource):
    def __init__(self):
        pass
    
    #Get profil client
    @jwt_required
    def get(self):
        claim = get_jwt_claims()
        qry = Clients.query.get(claim['id'])
        if qry is not None:
            return marshal(qry, Clients.response_fields), 200
        return {'status' : 'UNAUTHORIZED'}

    #Update profil client
    @jwt_required
    def put(self):
        claim = get_jwt_claims()
        qry = Clients.query.get(claim['id'])
        policy = PasswordPolicy.from_names(
            length = 8,
            numbers = 1,
            uppercase = 1
        )

        parser = reqparse.RequestParser()
        parser.add_argument('nama', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('no_telepon', location='json', required=True)
        parser.add_argument('no_rekening', location='json', required=True)
        parser.add_argument('lokasi', location='json', required=True)

        args = parser.parse_args()

        validation = policy.test(args['password'])

        if validation == []:
            password_digest = hashlib.md5(args['password'].encode()).hexdigest()
            
            qry.nama = args['nama']
            qry.password = password_digest
            qry.no_telepon = args['no_telepon']
            qry.no_rekening = args['no_rekening']
            qry.lokasi = args['lokasi']

            db.session.commit()

            return marshal(qry, Clients.response_fields), 200, {'Content-Type':'application/json'}
        return {'status' : 'UNAUTHORIZED'}

class ClientRegisterResource(Resource):

    #Register akun sebagai pembeli atau supplier
    def post(self):
        policy = PasswordPolicy.from_names(
            length = 8,
            numbers = 1,
            uppercase = 1
        )

        parser = reqparse.RequestParser()
        parser.add_argument('nama', location='json', required=True)
        parser.add_argument('no_telepon', location='json', required=True)
        parser.add_argument('no_rekening', location='json', required=True)
        parser.add_argument('lokasi', location='json', required=True)
        parser.add_argument('email', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('jenis_akun', location='json', required=True)

        args = parser.parse_args()

        validation = policy.test(args['password'])

        if validation == []:
            password_digest = hashlib.md5(args['password'].encode()).hexdigest()
            client = Clients(args['nama'], args['no_telepon'], args['no_rekening'], args['lokasi'], args['email'], password_digest, args['jenis_akun'])

            db.session.add(client)
            db.session.commit()

            app.logger.debug('DEBUG : %s', client)

            return marshal(client, Clients.response_fields), 200, {'Content-Type':'application/json'}

api.add_resource(ClientList,'/admin')
api.add_resource(ClientRegisterResource,'/register')
api.add_resource(ClientResource, '/user')


