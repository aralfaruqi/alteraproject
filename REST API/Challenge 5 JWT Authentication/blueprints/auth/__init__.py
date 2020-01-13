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
        parser.add_argument('client_key', location='args', required=True)
        parser.add_argument('client_secret', location='args', required=True)
        args = parser.parse_args()

        client_secret = hashlib.md5(args['client_secret'].encode()).hexdigest()

        if args['client_key'] == 'super_user' and args['client_secret'] == 'jUsT1ntern4l':
            token = create_access_token(identity=args['client_key'], user_claims={'status' : 'super_user'})
            return {'token' : token}, 200
        else:
            qry = Clients.query.filter_by(client_key=args['client_key']).filter_by(client_secret=client_secret)

            query_client = qry.first()
            if query_client is not None:
                query_client = marshal(query_client, Clients.jwt_claims_fields)
                query_client['status'] = 'normal_user'
                token = create_access_token(identity=args['client_key'], user_claims=query_client)
                return {'token' : token}, 200
            else:
                return {'status' : 'UNAUTHORIZED', 'message' : 'invalid key or secret'}, 401

api.add_resource(CreateTokenResource, '')