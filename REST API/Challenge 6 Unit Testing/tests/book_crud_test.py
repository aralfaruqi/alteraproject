import json
from . import *

class TestBookCrud():

    reset_db()

    def book_post_super_user(self, client):
        token = create_token(True)

        data = {
            'title' : 'Ilmu Saham',
            'category' : 'Bisnis',
            'author' : 'Alan Suryajana'
        }

        res = client.post('/book',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200
        assert res_json['id'] > 0
   
    def book_post_normal_user(self, client):
        token = create_token()

        data = {
            'title' : 'Ekonomi Syariah',
            'category' : 'Ekonomi',
            'author' : 'Artidjo Alkotsar'
        }

        res = client.post('/book',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 403

    def book_get_idfound_super_user(self, client):
        token = create_token(True)

        res = client.get('/book/3',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def book_get_idfound_normal_user(self, client):
        token = create_token()

        res = client.get('/book/1',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 403
    
    def book_get_idnotfound_super_user(self, client):
        token = create_token(True)

        res = client.get('/book/4',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 404

    def book_put_super_user(self, client):
        token = create_token(True)

        data = {
            'title' : 'Kisah kasih investasi',
            'category' : 'Romance',
            'author' : 'Budi Setiawan'
        }

        res = client.put('/book/1',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def book_put_super_user(self, client):
        token = create_token()

        data = {
            'title' : 'Riwayat Cerita',
            'category' : 'Drama',
            'author' : 'Raditya Dika'
        }

        res = client.put('/book/1',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 403

    def book_put_super_user_idnotfound(self, client):
        token = create_token(True)

        data = {
            'title' : 'Data Science Indo',
            'category' : 'Statistik',
            'author' : 'Mark Zaks'
        }

        res = client.put('/book/5',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 404

    #GET
    def book_getall_super_user(self, client):
        token = create_token(True)

        data = {
            'p' : 1,
            'rp' : 25,
            'author' : 'Budi',
            'orderby' : 'title',
            'sort' : 'asc'
        }

        res = client.get('/book',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def book_getall_super_user2(self, client):
        token = create_token(True)

        data = {
            'p' : 1,
            'rp' : 25,
            'author' : 'Budi',
            'orderby' : 'title',
            'sort' : 'desc'
        }

        res = client.get('/book',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def book_getall_super_user3(self, client):
        token = create_token(True)

        data = {
            'p' : 1,
            'rp' : 25,
            'author' : 'Zaks',
            'orderby' : 'category',
            'sort' : 'asc'
        }

        res = client.get('/book',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def book_getall_super_user4(self, client):
        token = create_token(True)

        data = {
            'p' : 1,
            'rp' : 25,
            'author' : 'Zaks',
            'orderby' : 'category',
            'sort' : 'desc'
        }

        res = client.get('/book',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def book_delete_super_user(self, client):
        token = create_token(True)

        res = client.delete('/book/1',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def book_delete_normal_user(self, client):
        token = create_token()

        res = client.delete('/book/1',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 403
    
    def book_delete_super_user_idnotfound(self, client):
        token = create_token(True)

        res = client.delete('/book/4',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 404
