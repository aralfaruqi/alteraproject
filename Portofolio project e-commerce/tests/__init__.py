# tests/__init__.py

import pytest, json, logging, hashlib
from flask import Flask, request

from blueprints import app, db
from blueprints.client.model import Clients
from blueprints.product.model import Products
from blueprints.transaction.model import Transactions
from blueprints.transaction_details.model import Transaction_detailss
from app import cache

def reset_db():
    db.drop_all()
    db.create_all()

    client = Clients("AdminToko","081245678901","567894028765","Jl. Kadal Gurun, malang","admin_toko@gmail.com","AdminToko123!","admin_toko")
    db.session.add(client)

    password_supplier1 = hashlib.md5("Supplier1123!".encode()).hexdigest()
    client = Clients("Supplier1","081245678901","567894028765","Jl. Kadal Gurun, malang","supplier1@gmail.com",password_supplier1,"supplier")
    db.session.add(client)

    password_pembeli1 = hashlib.md5("Pembeli1123!".encode()).hexdigest()
    client = Clients("Pembeli1","081230978901","876894028765","Jl. Pisang candi, malang","pembeli1@gmail.com",password_pembeli1,"pembeli")
    db.session.add(client)

    db.session.commit()

def call_client(request):
    client = app.test_client()
    return client

@pytest.fixture
def client(request):
    return call_client(request)

def create_token(jenis_akun):
    if jenis_akun == "admin_toko":
        cachename = 'test-admin-token'
        data = {
                'email': 'admin_toko@gmail.com',
                'password': 'AdminToko123!',
                'jenis_akun' : 'supplier'
            }
    elif jenis_akun == "supplier":
        cachename = 'test-supplier-token'
        data = {
                'email': 'supplier1@gmail.com',
                'password': 'Supplier1123!',
                'jenis_akun' : 'supplier'
            }
    elif jenis_akun == "pembeli" :
        cachename = 'test-pembeli-token'
        data = {
                'email': 'pembeli1@gmail.com',
                'password': 'Pembeli1123!',
                'jenis_akun' : 'pembeli'
            }
    
    token = cache.get(cachename)
    if token is None:
        ## do request
        req = call_client(request)
        res = req.get('/auth', 
                        json=data
        )
        
        ## store response
        res_json = json.loads(res.data)

        logging.warning('RESULT : %s', res_json)

        ## assert / compare with expected result
        assert res.status_code == 200

        ## save token into cache
        cache.set(cachename, res_json['token'], timeout=60)

        ## return, because it usefull for other test
        return res_json['token']
    else:
        return token
