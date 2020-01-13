import json
from . import *

class TestTransaction_detailsCrud():

    reset_db()

    def test_post_transaction_details(self, client):
        token = create_token("pembeli")

        data = {
            "product_id":1,
            "supplier_id":3,
            "nama_supplier":"Dagadu",
            "kuantitas": 1,
            "harga": 90000,
            "metode_pengiriman": "Fast Delivery 24 Jam"
        }

        res = client.post('/transaction_details/pembeli',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_put_transaction_details(self, client):
        token = create_token("supplier")

        data = {
            'product_id' : 1
        }


        res = client.put('/transaction_details/supplier',
                            json = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_all_list_transaction_details_admin(self, client):
        token = create_token("admin_toko")

        data = {
            'p' : 1,
            'rp' : 25,
            'product_id' : 1,
            'supplier_id' : 3
        }

        res = client.get('/transaction_details/admin',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200
    
