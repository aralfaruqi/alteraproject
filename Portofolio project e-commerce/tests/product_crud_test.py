import json
from . import *

class TestProductCrud():

    reset_db()

    def test_product_post(self, client):
        token = create_token("supplier")

        data = {
            "nama_produk":"Stick PS 2",
            "kategori":"Konsol gaming",
            "brand":"Microsoft",
            "harga": 70000,
            "lokasi_kota": "Malang",
            "harga_awal": 100000,
            "persen_discount": 30,
            "deskirpsi_produk": "Produk Mantap",
            "gratis_ongkir": True,
            "nama_supplier": "dagadu toko"
        }

        res = client.post('/product/supplier',
                         json=data,
                         headers={'Authorization' : 'Bearer ' + token}
                         )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_product_put(self, client):
        token = create_token("supplier")

        data = {
            "nama_produk":"Stick PS 3",
            "kategori":"Konsol gaming",
            "brand":"Microsoft",
            "harga": 100000,
            "lokasi_kota": "Malang",
            "harga_awal": 120000,
            "persen_discount": 30,
            "deskirpsi_produk": "Produk Mantap",
            "gratis_ongkir": True,
            "nama_supplier": "dagadu toko"
        }

        res = client.put('/product/supplier/1',
                         json=data,
                         headers={'Authorization' : 'Bearer ' + token}
                         )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_client_lihat_allproduct_admin1(self, client):

        data = {
            'p' : 1,
            'rp' : 25,
            'nama_produk' : 'Stick PS 2',
            'brand' : 'Microsoft',
            'lokasi_kota' : 'Malang',
            'persen_discount' : 30,
            'gratis_ongkir' : "True",
            'order_by' : 'harga',
            'sort' : 'asc'
        }

        res = client.get('/product/list',
                           query_string = data
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_client_lihat_allproduct_admin2(self, client):

        data = {
            'p' : 1,
            'rp' : 25,
            'nama_produk' : 'Stick PS 2',
            'brand' : 'Microsoft',
            'lokasi_kota' : 'Malang',
            'persen_discount' : 30,
            'gratis_ongkir' : "True",
            'order_by' : 'harga',
            'sort' : 'desc'
        }

        res = client.get('/product/list',
                        query_string = data
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_client_lihat_allproduct_admin3(self, client):

        data = {
            'p' : 1,
            'rp' : 25,
            'nama_produk' : 'Stick PS 2',
            'brand' : 'Microsoft',
            'lokasi_kota' : 'Malang',
            'persen_discount' : 30,
            'gratis_ongkir' : "True",
            'order_by' : 'persen_discount',
            'sort' : 'asc'
        }

        res = client.get('/product/list',
        query_string = data
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_client_lihat_allproduct_admin4(self, client):

        data = {
            'p' : 1,
            'rp' : 25,
            'nama_produk' : 'Stick PS 2',
            'brand' : 'Microsoft',
            'lokasi_kota' : 'Malang',
            'persen_discount' : 30,
            'gratis_ongkir' : "True",
            'order_by' : 'persen_discount',
            'sort' : 'desc'
        }

        res = client.get('/product/list',
        query_string = data
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

 

    
