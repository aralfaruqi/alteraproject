from datetime import datetime

class Client():

    def __init__(self):
        self.reset()

    def reset(self):
        self.created_at = None
        self.updated_at = None
        self.deleted_at = None
        self.client_id = 0
        self.client_key = None
        self.client_secret = None
        self.status = False

    def serialize(self):
        return { 
            "created_at" : self.created_at,
            "updated_at" : self.updated_at,
            "deleted_at" : self.deleted_at,
            "client_id" : self.client_id,
            "client_key" : self.client_key,
            "client_secret" : self.client_secret,
            "status" : self.status,
        }

class Clients():

    clients = []

    def __init__(self):
        for i in range(10):
            client = Client()
            client.client_id = i+1
            now = datetime.now()
            client.created_at = str(now)
            if i < 10:
                client.client_key = "CLIENT0"+str(i+1)
                client.client_secret = "SECRET0"+str(i+1)
            else:
                client.client_key = "CLIENT"+str(i+1)
                client.client_secret = "SECRET"+str(i+1)
            client.status = True
            self.clients.append(client.serialize())
    
    def get_all(self):
        return self.clients
    
    def get_one(self, id):
        for k, v in enumerate(self.clients) :
            if int(v['client_id']) == int(id):
                return v
        
        return None
    
    def delete_one(self, id):
        for k,v in enumerate(self.clients):
            if int(v['client_id']) == int(id):
                self.clients.pop(k)
    
    def post_one(self,post_serialize):
        return self.clients.append(post_serialize)
    
    def update(self,id,args):
        for k, v in enumerate(self.clients):
            if int(v['client_id']) == int(id):
                v['client_id'] = id
                v['client_secret'] = args['client_secret']
                v['client_key'] = args['client_key']
                v['status'] = args['status']
                now = datetime.now()
                v['updated_at'] = str(now)
                return v



        

    
