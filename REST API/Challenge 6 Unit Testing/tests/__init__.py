import pytest, json, logging, hashlib
from flask import Flask, request
from blueprints import app, db
from app import cache
from blueprints.client.model import Clients
from blueprints.book.model import Books
from blueprints.user.model import Users
from blueprints.rent.model import Rents

def reset_db():
    db.drop_all()
    db.create_all()

    client = Clients("user1",'jd48dm1069cjgu458j6f78ght5k5l0m1' , True)
    db.session.add(client)
    
    client = Clients("user2",'jd48dm1069cjgu458j6f78ght5k5l0m1' , True)
    db.session.add(client)
    db.session.commit()

    book = Books('Ilmu Saham', 'Bisnis', 'Alan Suryajana')
    db.session.add(book)
   
    book = Books('Trading Forex', 'Ekonomi', 'Edi Rahmayadi')
    db.session.add(book)
    db.session.commit()

    user = Users('achmad', 22, 'male', 1)
    db.session.add(user)
    
    user = Users('rafiq', 22, 'male', 1)
    db.session.add(user)
    db.session.commit()

def call_client(request):
    client = app.test_client()
    return client

@pytest.fixture
def client(request):
    return call_client(request)

def create_token(isinternal=False):
    if isinternal:
        cachename = 'test-internal-token'
        data = {
            'client_key' : 'super_user',
            'client_secret' : 'jUsT1ntern4l'
        }
    else:
        cachename = 'test-token'
        data = {
            'client_key' : 'user1',
            'client_secret' : 'user123'
        }

    token = cache.get(cachename)

    if token is None:
        req = call_client(request)
        res = req.get('/token', query_string = data)
        res_json = json.loads(res.data)
        logging.warning('RESULT : %s', res_json)
        assert res.status_code == 200

        cache.set(cachename, res_json['token'], timeout=60)
        return res_json['token']
    else:
        return token
         