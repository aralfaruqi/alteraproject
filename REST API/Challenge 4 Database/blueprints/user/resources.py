from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from sqlalchemy import desc
from datetime import datetime
from .model import Users
from blueprints import db, app

bp_user = Blueprint('user', __name__)
api = Api(bp_user)

class UserResource(Resource):
    def __init__(self):
        pass

    def get(self, id):
        qry = Users.query.get(id)
        if qry is not None:
            return marshal(qry, Users.response_fields), 200
        return {'status': 'NOT_FOUND'}, 404
    
    def put(self, id):
        parser = reqparse.RequestParser()
        qry = Users.query.get(id)
        parser.add_argument('client_id', location='json', required=True)
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('age', location='json', required=True)
        parser.add_argument('sex', location='json', required=True)
        args = parser.parse_args()

        qry.client_id = args['client_id']
        qry.name = args['name']
        qry.age = args['age']
        qry.age = args['sex']

        db.session.commit()

        return marshal(qry, Users.response_fields), 200, {'Content-Type': 'application/json'}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('client_id', location='json', required=True)
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('age', location='json', required=True)
        parser.add_argument('sex', location='json', required=True)

        args = parser.parse_args()
        
        user = Users(args['client_id'], args['name'], args['age'], args['sex'])
        db.session.add(user)
        db.session.commit()

        app.logger.debug('DEBUG : %s', )

        return marshal(user, Users.response_fields), 200, {'Content-Type' : 'application/json'}

    def delete(self,id):
        qry = Users.query.get(id)
        if qry is not None:
            db.session.delete(qry)
            db.session.commit()

            return  {'message':'deleted'}, 200
        return {'status': 'NOT_FOUND'}, 404
    
class UserList(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('age', location='args')
        parser.add_argument('sex', location='args')
        parser.add_argument('orderby', location='args', help='invalid order by value', choices=('name', 'age', 'sex', 'id'))
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc', 'asc'))

        args = parser.parse_args()

        offset = (args['p']*args['rp'] - args['rp'])

        # qry = Users.query.filter(Users.name.like("%"+args['name']+"%"))

        qry = Users.query

        if args['age'] is not None :
            qry = qry.filter_by(status=args['age'])
        
        if args['sex'] is not None :
            qry = qry.filter_by(status=args['sex'])

        if args['orderby'] is not None :
            if args['orderby'] == 'name':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Users.name))
                else:
                    qry = qry.order_by(Users.name)
            
            elif args['orderby'] == 'age' :
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Users.age))
                else:
                    qry = qry.order_by(Users.age)
            
            elif args['orderby'] == 'sex' :
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Users.sex))
                else:
                    qry = qry.order_by(Users.sex)

            elif args['orderby'] == 'id' :
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Users.id))
                else:
                    qry = qry.order_by(Users.id)
                

        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Users.response_fields))
        
        return rows, 200

api.add_resource(UserList, '', '/list')
api.add_resource(UserResource, '', '/<id>')