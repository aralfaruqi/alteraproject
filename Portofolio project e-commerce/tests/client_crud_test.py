import json
from . import *

class TestClientCrud():

    reset_db()

    def test_supplier_register(self, client):

        data = {
            "nama":"Supplier45",
            "no_telepon":"081245678901",
            "no_rekening":"567894028765",
            "lokasi": "Jl. Kadal Gurun, malang",
            "email": "supplier45@gmail.com",
            "password": "Supplier8123!",
            "jenis_akun": "supplier"
        }

        res = client.post('/client/register',
                         json=data,
                         )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_pembeli_register(self, client):

        data = {
            "nama":"Pembeli45",
            "no_telepon":"081230978901",
            "no_rekening":"876894028765",
            "lokasi": "Jl. Pisang candi, malang",
            "email": "pembeli45@gmail.com",
            "password": "Pembeli8123!",
            "jenis_akun": "pembeli"
        }

        res = client.post('/client/register',
                         json=data,
                         )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_client_lihat_profil_pembeli(self, client):
        token = create_token("pembeli")

        res = client.get('/client/user',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_client_lihat_profil_supplier(self, client):
        token = create_token("supplier")

        res = client.get('/client/user',
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200
    
    def test_client_lihat_allprofil_admin1(self, client):
        token = create_token("admin_toko")

        data = {
            'p' : 1,
            'rp' : 25,
            'orderby' : 'id',
            'jenis_akun' : 'pembeli',
            'sort' : 'asc'
        }

        res = client.get('/client/admin',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_client_lihat_allprofil_admin2(self, client):
        token = create_token("admin_toko")

        data = {
            'p' : 1,
            'rp' : 25,
            'orderby' : 'id',
            'jenis_akun' : 'pembeli',
            'sort' : 'desc'
        }

        res = client.get('/client/admin',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_client_lihat_allprofil_admin3(self, client):
        token = create_token("admin_toko")

        data = {
            'p' : 1,
            'rp' : 25,
            'orderby' : 'created_at',
            'jenis_akun' : 'pembeli',
            'sort' : 'asc'
        }

        res = client.get('/client/admin',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_client_lihat_allprofil_admin4(self, client):
        token = create_token("admin_toko")

        data = {
            'p' : 1,
            'rp' : 25,
            'orderby' : 'created_at',
            'jenis_akun' : 'pembeli',
            'sort' : 'desc'
        }

        res = client.get('/client/admin',
                            query_string = data,
                            headers={'Authorization' : 'Bearer ' + token}
                            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_supplier_put(self, client):
        token = create_token("supplier")

        data = {
            "nama":"Mang Ujang",
            "password":"Bersatu123!",
            "no_telepon":"039201092019210",
            "no_rekening": "4768393002930",
            "lokasi": "Malang",
            "harga_awal": 120000,
            "persen_discount": 30,
            "deskirpsi_produk": "Produk Mantap",
            "gratis_ongkir": True,
            "nama_supplier": "dagadu toko"
        }

        res = client.put('/client/user',
                         json=data,
                         headers={'Authorization' : 'Bearer ' + token}
                         )
        res_json = json.loads(res.data)
        assert res.status_code == 200

 

    
