from flask import Blueprint
from flask_restful import Api, reqparse, Resource

from . import *

bp_client = Blueprint('client', __name__)
api = Api(bp_client)

class ClientResource(Resource):

    clients = Clients()

    def get(self,id=None):
        if id is None :
            return self.clients.get_all(), 200, {'Content-Type': 'application/json'}
        else:
            return self.clients.get_one(id), 200, {'Content-Type': 'application/json'}
    
    def delete(self,id):
        self.clients.delete_one(id)
        return {'message':'deleted'}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='json')
        parser.add_argument('client_secret', location='json')
        parser.add_argument('status', location='json')
        args = parser.parse_args()

        client = Client()
        client.client_id = self.clients.clients[-1]['client_id']+1
        client.client_key = 'CLIENT'+str(self.clients.clients[-1]['client_id']+1)
        client.client_secret = 'CLIENT'+str(self.clients.clients[-1]['client_id']+1)
        client.status = True

        self.clients.post_one(client.serialize())
        return client.serialize(), 200, {'Content-Type':'application/json'}
    
    def put(self,id):
        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='json')
        parser.add_argument('client_secret', location='json')
        parser.add_argument('status', location='json')
        args = parser.parse_args()

        hasil = self.clients.update(id,args)

        return hasil, 200, {'Content-Type':'application/json'}

        



    # def post(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('name', location='json', required=True)
    #     parser.add_argument('age', location='json', type=int, required=True)
    #     parser.add_argument('sex', location='json')
    #     args = parser.parse_args()

    #     self.person.name = args['name']
    #     self.person.age = args['age']
    #     self.person.sex = args['sex']
    
    #     return self.person.__dict__, 200, {'Content-Type': 'application/json'}

    # def put(self):
    #     return self.person.__dict__, 200, {'Content-Type': 'application/json'}

    # def delete(self):
    #     self.person = Person()
    #     return 'Deleted', 200

    # def patch(self):
    #     return 'Not yet implemented', 501

api.add_resource(ClientResource, '', '/<id>')