from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from sqlalchemy import desc
from datetime import datetime
from .model import Clients
from blueprints import db, app

bp_client = Blueprint('client', __name__)
api = Api(bp_client)

class ClientResource(Resource):
    def __init__(self):
        pass

    def get(self, id):
        qry = Clients.query.get(id)
        if qry is not None:
            return marshal(qry, Clients.response_fields), 200
        return {'status': 'NOT_FOUND'}, 404
    
    def put(self, id):
        parser = reqparse.RequestParser()
        qry = Clients.query.get(id)
        parser.add_argument('client_key', location='json', required=True)
        parser.add_argument('client_secret', location='json', required=True)
        parser.add_argument('status', type=inputs.boolean, location='json', required=True)
        args = parser.parse_args()

        qry.client_key = args['client_key']
        qry.client_secret = args['client_secret']
        qry.status = args['status']

        db.session.commit()

        return marshal(qry, Clients.response_fields), 200, {'Content-Type': 'application/json'}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='json', required=True)
        parser.add_argument('client_secret', location='json', required=True)
        parser.add_argument('status', type=inputs.boolean, location='json', required=True)

        args = parser.parse_args()

        client = Clients(args['client_key'], args['client_secret'], args['status'])
        db.session.add(client)
        db.session.commit()

        app.logger.debug('DEBUG : %s', client)

        return marshal(client, Clients.response_fields), 200, {'Content-Type' : 'application/json'}

    def delete(self,id):
        qry = Clients.query.get(id)
        if qry is not None:
            db.session.delete(qry)
            db.session.commit()

            return  {'message':'deleted'}, 200
        return {'status': 'NOT_FOUND'}, 404
    
class ClientList(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('status', location='args', help='invalid status', choices=(True, False))
        parser.add_argument('orderby', location='args', help='invalid order by value', choices=('client_key', 'client_secret', 'id'))
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc', 'asc'))

        args = parser.parse_args()

        offset = (args['p']*args['rp'] - args['rp'])

        # qry = Clients.query.filter(Clients.name.like("%"+args['name']+"%"))

        qry = Clients.query

        if args['status'] is not None :
            qry = qry.filter_by(status=args['status'])

        if args['orderby'] is not None :
            if args['orderby'] == 'client_key':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Clients.client_key))
                else:
                    qry = qry.order_by(Clients.client_key)
            
            elif args['orderby'] == 'client_secret' :
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Clients.client_secret))
                else:
                    qry = qry.order_by(Clients.client_secret)

            elif args['orderby'] == 'id' :
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Clients.id))
                else:
                    qry = qry.order_by(Clients.id)
                

        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Clients.response_fields))
        
        return rows, 200

api.add_resource(ClientList, '', '/list')
api.add_resource(ClientResource, '', '/<id>')

    