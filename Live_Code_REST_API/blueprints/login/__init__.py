from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims

from ..penerbit.model import Penerbits

bp_login = Blueprint('login', __name__)
api = Api(bp_login)

class CreateTokenResource(Resource):

    def post(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='args', required=True)
        parser.add_argument('client_secret', location='args', required=True)
        args = parser.parse_args()

        if args['client_key'] == 'internal' and args['client_secret'] == 'th1s1s1nt3n4lcl13nt':
            token = create_access_token(identity=args['client_key'],user_claims={'data':"ini_admin","isinternal":True})
            return {'token': token}, 200
        else:
            qry = Penerbits.query.filter_by(client_key=args['client_key']).filter_by(client_secret=args['client_secret'])

            clientData = qry.first()
            if clientData is not None :
                clientData = marshal(clientData, Clients.jwt_claims_fields)
                clientData['data']='ini_public'
                clientData['isinternal'] = False
                token = create_access_token(identity=clientData["client_key"], user_claims=clientData)
                return {'token': token}, 200
            else:
                return {'status': 'UNAUTHORIZED', 'message': 'invalid key or secret'}, 401

api.add_resource(CreateTokenResource, '')
