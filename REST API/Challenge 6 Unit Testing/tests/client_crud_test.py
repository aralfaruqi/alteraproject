import json
from . import *

class TestClientCrud():

    reset_db()

    def client_post_super_user(self, client):
        token = create_token(True)

        data = {
            'client_key' : 'user1',
            'client_secret' : 'user123',
            'status' : True
        }

        res = client.post('/client',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200
        assert res_json['id'] > 0
    
    def client_post_normal_user(self, client):
        token = create_token()

        data = {
            'client_key' : 'user1',
            'client_secret' : 'user123',
            'status' : 'true'
        }

        res = client.post('/client',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 403

    def client_get_idfound_super_user(self, client):
        token = create_token(True)

        res = client.get('/client/1',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def user_get_idfound_normal_user(self, client):
        token = create_token()

        res = client.get('/user/1',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 403
    
    def client_get_idnotfound_super_user(self, client):
        token = create_token(True)

        res = client.get('/client/4',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 404

    def client_put_super_user(self, client):
        token = create_token(True)

        data = {
            'client_key' : 'thisiskey',
            'client_secret' : 'thisissecret123',
            'status' : True
        }

        res = client.put('/client/1',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def client_put_normal_user(self, client):
        token = create_token()

        data = {
            'client_key' : 'thisisnormal',
            'client_secret' : 'thisisnormal123',
            'status' : True
        }

        res = client.put('/client/1',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 403

    def client_put_super_user_idnotfound(self, client):
        token = create_token(True)

        data = {
            'client_key' : 'thisiskey',
            'client_secret' : 'thisiskey123',
            'status' : True
        }

        res = client.put('/client/5',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 404

    def client_getall_super_user(self, client):
        token = create_token(True)

        data = {
            'p' : 1,
            'rp' : 25,
            'status' : False,
            'orderby' : 'id',
            'sort' : 'asc'
        }

        res = client.get('/client',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def client_getall_super_user2(self, client):
        token = create_token(True)

        data = {
            'p' : 1,
            'rp' : 25,
            'status' : True,
            'orderby' : 'id',
            'sort' : 'desc'
        }

        res = client.get('/client',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def client_getall_super_user3(self, client):
        token = create_token(True)

        data = {
            'p' : 1,
            'rp' : 25,
            'status' : True,
            'orderby' : 'client_key',
            'sort' : 'asc'
        }

        res = client.get('/client',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def client_getall_super_user4(self, client):
        token = create_token(True)

        data = {
            'p' : 1,
            'rp' : 25,
            'status' : True,
            'orderby' : 'client_key',
            'sort' : 'desc'
        }

        res = client.get('/client',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def client_delete_super_user(self, client):
        token = create_token(True)

        res = client.delete('/client/2',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def client_delete_normal_user(self, client):
        token = create_token()

        res = client.delete('/client/4',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 403
    
    def client_delete_super_user_idnotfound(self, client):
        token = create_token(True)

        res = client.delete('/client/4',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 404
