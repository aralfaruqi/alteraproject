import json
from . import *

class TestRentCrud():

    reset_db()

    def rent_post(self, client):
        token = create_token(True)

        data = {
            'book_id' : 1,
            'user_id' : 1 
        }

        res = client.post('/rent',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200
        assert res_json['id'] > 0
   
    def rent_get_idfound_super_user(self, client):
        token = create_token(True)

        res = client.get('/rent/1',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 401

    def rent_getall_super_user(self, client):
        token = create_token(True)

        data = {
            'p' : 1,
            'rp' : 25,
            'user_id' : 1,
            'book_id' : 1
        }

        res = client.get('/rent',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

   