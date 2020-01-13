from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from sqlalchemy import desc
from .model import Rents
from blueprints.user.model import Users
from blueprints.book.model import Books
from blueprints.client.model import Clients
from blueprints import db,app, internal_required
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_rent = Blueprint('rent', __name__)
api = Api(bp_rent)

class RentList(Resource):
    def __init__(self):
        pass

    @jwt_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('user_id', type=int, location='args')
        parser.add_argument('book_id', type=int, location='args')

        args = parser.parse_args()

        offset = (args['p']*args['rp'])-args['rp']

        qry_rent = Rents.query

        if args['user_id'] is not None:
            qry_rent = qry_rent.filter_by(user_id=args['user_id'])
        
        if args['book_id'] is not None:
            qry_rent = qry_rent.filter_by(book_id=args['user_id'])

        rows = []
        claim = get_jwt_claims()
        if claim['status'] == 'normal_user':
            qry_client = Clients.query.filter_by(client_key=claim['client_key']).first()
            qry_user = Users.query.filter_by(client_id=qry_client.id)
            for query_user in qry_user:
                qry_rent_final = qry_rent.filter_by(user_id=query_user.id).limit(args['rp']).offset(offset)

                for query_rent in qry_rent_final:
                    marshalRent = marshal(query_rent, Rents.response_fields)

                    qry_book = Books.query.get(marshalRent['book_id'])
                    marshalBook = marshal(qry_book, Books.response_fields)

                    marshalUser = marshal(query_rent, Users.response_fields)

                    marshalRent['user'] = marshalUser
                    marshalRent['book'] = marshalBook
                    rows.append(marshalRent)
            
            return rows, 200, {'Content-Type':'application/json'}
        return {'status' : 'UNAUTHORIZED'}


class RentResource(Resource):
    def __init__(self):
        pass

    @jwt_required
    def get(self, id):
        claim = get_jwt_claims()
        if claim['status'] == 'normal_user':
            qry_rent = Rents.query.get(id)
            marshalRent = marshal(qry_rent, Rents.response_fields)

            qry_client = Clients.query.filter_by(client_key=claim['client_key']).first()
            marshalClients = marshal(qry_client, Clients.response_fields)

            qry_user = Users.query.filter_by(client_id=marshalClients['id'])
            
            for query_user in qry_user:
                if marshalRent['user_id'] == query_user.id:
                    marshalUser = marshal(query_user, Users.response_fields)
                    qry_book = Books.query.get(marshalRent['book_id'])
                    marshalBook = marshal(qry_book, Books.response_fields)

                    marshalRent['user'] = marshalUser
                    marshalRent['book'] = marshalBook

                    return marshalRent, 200, {'Content-Type':'application/json'}
        return {'status' : 'UNAUTHORIZED'}

        
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('book_id', location='json', required=True)
        parser.add_argument('user_id', location='json', required=True)

        args = parser.parse_args()

        rent = Rents(args['book_id'], args['user_id'])
        db.session.add(rent)
        db.session.commit()

        app.logger.debug('DEBUG : %s', rent)

        return marshal(rent, Rents.response_fields), 200, {'Content-Type':'application/json'}

api.add_resource(RentList, '','/list')
api.add_resource(RentResource, '','/<id>')
