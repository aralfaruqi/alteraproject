from blueprints import db,app, internal_required
from flask_jwt_extended import jwt_required
from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from sqlalchemy import desc
from .model import Books

bp_book = Blueprint('book', __name__)
api = Api(bp_book)

class BookList(Resource):
    def __init__(self):
        pass
    
    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('author', location='args')
        parser.add_argument('orderby', location='args', help='invalid order value', choices=('title', 'id', 'category'))
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc','asc'))

        args = parser.parse_args()

        offset = (args['p']*args['rp'])-args['rp']

        qry = Books.query

        if args['author'] is not None:
            qry = qry.filter_by(author=args['author'])

        if args['orderby'] is not None:
            if args['orderby'] =='id':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Books.id))
                else:
                    qry = qry.order_by(Books.id)
            elif args['orderby'] =='title':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Books.title))
                else:
                    qry = qry.order_by(Books.title)
            elif args['orderby'] =='category':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Books.category))
                else:
                    qry = qry.order_by(Books.category)

        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Books.response_fields))
        
        return rows, 200

class BookResource(Resource):
    def __init__(self):
        pass
    
    @jwt_required
    @internal_required
    def get(self, id):
        qry = Books.query.get(id)
        if qry is not None:
            return marshal(qry, Books.response_fields), 200
        return {'status': 'NOT_FOUND'}, 404

    @jwt_required
    @internal_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', location='json', required=True)
        parser.add_argument('category', location='json', required=True)
        parser.add_argument('author', location='json', required=True)

        args = parser.parse_args()

        book = Books(args['title'], args['category'], args['author'])
        db.session.add(book)
        db.session.commit()

        app.logger.debug('DEBUG : %s', book)

        return marshal(book, Books.response_fields), 200, {'Content-Type':'application/json'}

    @jwt_required
    @internal_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', location='json', required=True)
        parser.add_argument('category', location='json', required=True)
        parser.add_argument('author', location='json', required=True)

        args = parser.parse_args()

        qry = Books.query.get(id)
        if qry is None:
            return {'status': 'NOT_FOUND'}, 404
        
        qry.title = args['title']
        qry.category = args['category']
        qry.author = args['author']
        db.session.commit()

        return marshal(qry, Books.response_fields), 200, {'Content-Type':'application/json'}

    @jwt_required
    @internal_required
    def delete(self, id):
        qry = Books.query.get(id)
        if qry is None:
            return {'status' : 'NOT_FOUND'}, 404

        db.session.delete(qry)
        db.session.commit()

api.add_resource(BookList, '','/list')
api.add_resource(BookResource, '','/<id>')

