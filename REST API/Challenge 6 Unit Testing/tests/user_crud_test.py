import json
from . import *

class TestUserCrud():

    reset_db()

    def user_post_super_user(self, client):
        token = create_token(True)

        data = {
            'name' : 'Rafiq',
            'age' : 22,
            'sex' : 'male',
            'client_id' : 1
        }

        res = client.post('/user',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200
        assert res_json['id'] > 0
    
    def user_post_normal_user(self, client):
        token = create_token()

        data = {
            'name' : 'Rafiq',
            'age' : 22,
            'sex' : 'male',
            'client_id' : 1
        }

        res = client.post('/user',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 403

    def user_get_idfound_super_user(self, client):
        token = create_token(True)

        res = client.get('/user/1',
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
    
    def user_get_idnotfound_super_user(self, client):
        token = create_token(True)

        res = client.get('/user/4',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 404

    def user_put_super_user(self, client):
        token = create_token(True)

        data = {
            'name' : 'Vicky',
            'age' : 22,
            'sex' : 'female',
            'client_id' : 2
        }

        res = client.put('/user/1',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def user_put_normal_user(self, client):
        token = create_token()

        data = {
            'name' : 'Vicky',
            'age' : 22,
            'sex' : 'female',
            'client_id' : 2
        }

        res = client.put('/user/1',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 403

    def user_put_super_user_idnotfound(self, client):
        token = create_token(True)

        data = {
            'name' : 'Vicky',
            'age' : 22,
            'sex' : 'female',
            'client_id' : 2
        }

        res = client.put('/user/5',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 404

    def user_getall_super_user(self, client):
        token = create_token(True)

        data = {
            'p' : 1,
            'rp' : 25,
            'sex' : 'male',
            'orderby' : 'age',
            'sort' : 'asc'
        }

        res = client.get('/user',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def user_getall_super_user2(self, client):
        token = create_token(True)

        data = {
            'p' : 1,
            'rp' : 25,
            'sex' : 'Male',
            'orderby' : 'age',
            'sort' : 'desc'
        }

        res = client.get('/user',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def user_getall_super_user3(self, client):
        token = create_token(True)

        data = {
            'p' : 1,
            'rp' : 25,
            'sex' : 'Male',
            'orderby' : 'id',
            'sort' : 'desc'
        }

        res = client.get('/user',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def user_getall_super_user4(self, client):
        token = create_token(True)

        data = {
            'p' : 1,
            'rp' : 25,
            'sex' : 'Male',
            'orderby' : 'id',
            'sort' : 'asc'
        }

        res = client.get('/user',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def user_delete_super_user(self, client):
        token = create_token(True)

        res = client.delete('/user/1',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def user_delete_normal_user(self, client):
        token = create_token()

        res = client.delete('/user/1',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 403
    
    def user_delete_super_user_idnotfound(self, client):
        token = create_token(True)

        res = client.delete('/user/4',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 404
