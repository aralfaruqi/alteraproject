from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from ..client.model import Clients
import json, hashlib

bp_auth = Blueprint('auth', __name__)
api = Api(bp_auth)

class CreateTokenResource(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('jenis_akun', location='json', required=True)

        args = parser.parse_args()

        password = hashlib.md5(args['password'].encode()).hexdigest()

        if args['email'] == 'admin_toko@gmail.com' and args['password'] == 'AdminToko123!' and args['jenis_akun'] == 'supplier' : 
            token = create_access_token(identity=args['email'], user_claims={'jenis_akun' : 'admin_toko'})
            return {'token' : token}, 200
        elif args['jenis_akun'] == 'supplier': 
            qry = Clients.query.filter_by(email=args['email']).filter_by(password=password)

            query_client = qry.first()
            if query_client is not None:
                query_client = marshal(query_client, Clients.jwt_claims_fields)
                query_client['jenis_akun'] = 'supplier'
                token = create_access_token(identity=args['email'], user_claims=query_client)
                return {'token' : token}, 200
            else:
                return {'status' : 'UNAUTHORIZED', 'message' : 'invalid key or secret'}, 401
        
        elif args['jenis_akun'] == 'pembeli': 
            qry = Clients.query.filter_by(email=args['email']).filter_by(password=password)

            query_client = qry.first()
            if query_client is not None:
                query_client = marshal(query_client, Clients.jwt_claims_fields)
                query_client['jenis_akun'] = 'pembeli'
                token = create_access_token(identity=args['email'], user_claims=query_client)
                return {'token' : token}, 200
            else:
                return {'status' : 'UNAUTHORIZED', 'message' : 'invalid key or secret'}, 401

api.add_resource(CreateTokenResource, '')