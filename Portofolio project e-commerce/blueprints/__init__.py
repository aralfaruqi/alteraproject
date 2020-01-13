from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims
import json, os
from datetime import timedelta
from functools import wraps

app = Flask(__name__)

app.config['APP_DEBUG'] = True
app.config['JWT_SECRET_KEY'] = 'njnFTsdiMDni7632jk3lNeu'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)

jwt = JWTManager(app)


def internal_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['jenis_akun'] != 'admin_toko':
            return {'status' : 'FORBIDDEN', 'message' : 'Internal Only!'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper

def supplier_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['jenis_akun'] != 'supplier':
            return {'status' : 'FORBIDDEN', 'message' : 'Internal Only!'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper

def pembeli_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['jenis_akun'] != 'pembeli':
            return {'status' : 'FORBIDDEN', 'message' : 'Internal Only!'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper

################
# DATABASE
################
try:
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'testing':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/testing_ecommerce'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/ecommerce_challenge'
except Exception as e:
    raise e
        
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.after_request
def after_request(response):
    try:
        requestData = request.get_json()
    except Exception as e:
        requestData = request.args.to_dict()
    
    if response.status_code == 200:
        app.logger.info("REQUEST_LOG\t%s", json.dumps({
            'status_code' : response.status_code,
            'method' : request.method,
            'code' : response.status,
            'uri' : request.full_path,
            'request': request.args.to_dict(),
            'responese': json.loads(response.data.decode('utf-8'))
            })
        )
    else:
        app.logger.error("REQUEST_LOG\t%s", json.dumps({
            'status_code' : response.status_code,
            'method' : request.method,
            'code' : response.status,
            'uri' : request.full_path,
            'request': request.args.to_dict(), 
            'responese': json.loads(response.data.decode('utf-8'))
            })
        )
    return response


from blueprints.product.resource import bp_product
app.register_blueprint(bp_product, url_prefix = '/product')

from blueprints.client.resource import bp_client
app.register_blueprint(bp_client, url_prefix = '/client')

from blueprints.transaction.resource import bp_transaction
app.register_blueprint(bp_transaction, url_prefix = '/transaction')

from blueprints.transaction_details.resource import bp_transaction_details
app.register_blueprint(bp_transaction_details, url_prefix = '/transaction_details')

from blueprints.auth import bp_auth
app.register_blueprint(bp_auth, url_prefix='/auth')

db.create_all()