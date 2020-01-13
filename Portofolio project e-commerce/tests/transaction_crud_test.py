import json
from . import *

class TestTransactionCrud():

    reset_db()

    def test_post_transaction(self, client):
        token = create_token("pembeli")

        res = client.post('/transaction/pembeli',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200
    
    def test_put_transaction(self, client):
        token = create_token("pembeli")

        data = {
            'Metode Pembayaran' : "Bank BRI"
        }


        res = client.put('/transaction/pembeli',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200
    
    def test_all_list_transaction_admin(self, client):
        token = create_token("admin_toko")

        data = {
            'p' : 1,
            'rp' : 25,
            'pembeli_id' : 1
        }

        res = client.get('/transaction/admin',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200
    



