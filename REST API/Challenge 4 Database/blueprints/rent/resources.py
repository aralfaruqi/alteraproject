from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from sqlalchemy import desc
from datetime import datetime
from .model import Rents
from blueprints.user.model import Users
from blueprints.book.model import Books
from blueprints import db, app

bp_rent = Blueprint('rent', __name__)
api = Api(bp_rent)

class RentResource(Resource):
    def __init__(self):
        pass

    def get(self, id):
        qry = Rents.query.get(id)
        if qry is not None:
            marshalRent = marshal(qry, Rents.response_fields)
            query_book = Books.query.get(marshalRent['book_id'])
            marshalBook = marshal(query_book, Books.response_fields)
            query_user = Users.query.get(marshalRent['user_id'])
            marshalUser = marshal(query_user, Users.response_fields)

            marshalRent['user'] = marshalUser
            marshalRent['book'] = marshalBook

            return marshalRent, 200, {'Content-Type' : 'application/json'}
        return {'status': 'NOT_FOUND'}, 404
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('book_id', location='json', required=True)
        parser.add_argument('user_id', location='json', required=True)

        args = parser.parse_args()
        
        rent = Rents(args['user_id'], args['book_id'])
        
        marshalRent = marshal(rent, Rents.response_fields)
        query_book = Books.query.get(marshalRent['book_id'])
        marshalBook = marshal(query_book, Books.response_fields)
        query_user = Users.query.get(marshalRent['user_id'])
        marshalUser = marshal(query_user, Users.response_fields)

        marshalRent['user'] = marshalUser
        marshalRent['book'] = marshalBook

        db.session.add(rent)
        db.session.commit()

        app.logger.debug('DEBUG : %s', )

        return marshalRent, 200, {'Content-Type' : 'application/json'}

    
class RentList(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('book_id', location='args')
        parser.add_argument('user_id', location='args')
        parser.add_argument('orderby', location='args', help='invalid order by value', choices=('book_id', 'user_id', 'id'))
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc', 'asc'))

        args = parser.parse_args()

        offset = (args['p']*args['rp'] - args['rp'])

        # qry = Books.query.filter(Books.name.like("%"+args['name']+"%"))

        qry = Rents.query

        if args['book_id'] is not None :
            qry = qry.filter_by(status=args['book_id'])
        
        if args['user_id'] is not None :
            qry = qry.filter_by(status=args['user_id'])

        if args['orderby'] is not None :
            if args['orderby'] == 'book_id':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Rents.book_id))
                else:
                    qry = qry.order_by(Rents.book_id)
            
            elif args['orderby'] == 'user_id' :
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Rents.user_id))
                else:
                    qry = qry.order_by(Rents.user_id)
            
            elif args['orderby'] == 'id' :
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Rents.id))
                else:
                    qry = qry.order_by(Rents.id)
        
        qrys = Rents.query.all()
        rows = []
        for qry in qrys:
            marshalRent = marshal(qry, Rents.response_fields)

            qry_book = Books.query.get(marshalRent['book_id'])
            marshalBook = marshal(qry_book, Books.response_fields)
            qry_user = Users.query.get(marshalRent['user_id'])
            marshalUser = marshal(qry_user, Users.response_fields)

            marshalRent['user'] = marshalUser
            marshalRent['book'] = marshalBook
            rows.append(marshalRent)
        
        return rows, 200, {'Content-Type':'application/json'}

api.add_resource(RentList, '', '/list')
api.add_resource(RentResource, '', '/<id>')