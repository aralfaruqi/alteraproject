from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from sqlalchemy import desc
from datetime import datetime
from .model import Books
from blueprints import db, app

bp_book = Blueprint('book', __name__)
api = Api(bp_book)

class BookResource(Resource):
    def __init__(self):
        pass

    def get(self, id):
        qry = Books.query.get(id)
        if qry is not None:
            return marshal(qry, Books.response_fields), 200
        return {'status': 'NOT_FOUND'}, 404
    
    def put(self, id):
        parser = reqparse.RequestParser()
        qry = Books.query.get(id)
        parser.add_argument('title', location='json', required=True)
        parser.add_argument('isbn', location='json', required=True)
        parser.add_argument('writer',location='json', required=True)
        args = parser.parse_args()

        qry.title = args['title']
        qry.isbn = args['isbn']
        qry.writer = args['writer']

        db.session.commit()

        return marshal(qry, Books.response_fields), 200, {'Content-Type': 'application/json'}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', location='json', required=True)
        parser.add_argument('isbn', location='json', required=True)
        parser.add_argument('writer', location='json', required=True)

        args = parser.parse_args()

        book = Books(args['title'], args['isbn'], args['writer'])
        db.session.add(book)
        db.session.commit()

        app.logger.debug('DEBUG : %s', book)

        return marshal(book, Books.response_fields), 200, {'Content-Type' : 'application/json'}

    def delete(self,id):
        qry = Books.query.get(id)
        if qry is not None:
            db.session.delete(qry)
            db.session.commit()

            return  {'message':'deleted'}, 200
        return {'status': 'NOT_FOUND'}, 404
    
class BookList(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('title', location='args')
        parser.add_argument('isbn', location='args')
        parser.add_argument('orderby', location='args', help='invalid order by value', choices=('title', 'isbn', 'writer' 'id'))
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc', 'asc'))

        args = parser.parse_args()

        offset = (args['p']*args['rp'] - args['rp'])

        # qry = Books.query.filter(Books.title.like("%"+args['title']+"%"))

        qry = Books.query

        if args['title'] is not None :
            qry = qry.filter_by(title=args['title'])
        
        if args['isbn'] is not None :
            qry = qry.filter_by(isbn=args['isbn'])
        

        if args['orderby'] is not None :
            if args['orderby'] == 'title':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Books.title))
                else:
                    qry = qry.order_by(Books.title)
            
            elif args['orderby'] == 'isbn' :
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Books.isbn))
                else:
                    qry = qry.order_by(Books.isbn)
            
            elif args['orderby'] == 'writer' :
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Books.writer))
                else:
                    qry = qry.order_by(Books.writer)

            elif args['orderby'] == 'id' :
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Books.id))
                else:
                    qry = qry.order_by(Books.id)
                

        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Books.response_fields))
        
        return rows, 200

api.add_resource(BookList, '', '/list')
api.add_resource(BookResource, '', '/<id>')