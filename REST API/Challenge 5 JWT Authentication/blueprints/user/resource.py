from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from sqlalchemy import desc
from .model import Users
from blueprints import db,app, internal_required
from flask_jwt_extended import jwt_required

bp_user = Blueprint('user', __name__)
api = Api(bp_user)

class UserList(Resource):
    def __init__(self):
        pass

    @jwt_required
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('sex', location='args')
        parser.add_argument('orderby', location='args', help='invalid order value', choices=('age', 'id', 'name', 'client_id'))
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc','asc'))

        args = parser.parse_args()

        offset = (args['p']*args['rp'])-args['rp']
        qry = Users.query

        if args['sex'] is not None:
            qry = qry.filter_by(sex=args['sex'])

        if args['orderby'] is not None:
            if args['orderby'] =='id':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Users.id))
                else:
                    qry = qry.order_by(Users.id)
            elif args['orderby'] =='name':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Users.name))
                else:
                    qry = qry.order_by(Users.name)
            elif args['orderby'] =='age':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Users.age))
                else:
                    qry = qry.order_by(Users.age)
            elif args['orderby'] =='client_id':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Users.client_id))
                else:
                    qry = qry.order_by(Users.client_id)

        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Users.response_fields))
        
        return rows, 200

        
class UserResource(Resource):
    def __init__(self):
        pass
    
    @jwt_required
    @internal_required
    def get(self, id):
        qry = Users.query.get(id)
        if qry is not None:
            return marshal(qry, Users.response_fields), 200
        return {'status': 'NOT_FOUND'}, 404

    @jwt_required
    @internal_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('age', location='json', required=True)
        parser.add_argument('sex', location='json', required=True)
        parser.add_argument('client_id', location='json', required=True)

        args = parser.parse_args()

        user = Users(args['name'], args['age'], args['sex'], args['client_id'])
        db.session.add(user)
        db.session.commit()

        app.logger.debug('DEBUG : %s', user)

        return marshal(user, Users.response_fields), 200, {'Content-Type':'application/json'}

    @jwt_required
    @internal_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('age', location='json', required=True)
        parser.add_argument('sex', location='json', required=True)
        parser.add_argument('client_id', location='json', required=True)

        args = parser.parse_args()

        qry = Users.query.get(id)
        if qry is None:
            return {'status': 'NOT_FOUND'}, 404
        
        qry.name = args['name']
        qry.age = args['age']
        qry.sex = args['sex']
        qry.sex = args['client_id']
        db.session.commit()

        return marshal(qry, Users.response_fields), 200, {'Content-Type':'application/json'}

    @jwt_required
    @internal_required
    def delete(self, id):
        qry = Users.query.get(id)
        if qry is None:
            return {'status' : 'NOT_FOUND'}, 404
    
        db.session.delete(qry)
        db.session.commit()

api.add_resource(UserList, '','/list')
api.add_resource(UserResource, '','/<id>')
