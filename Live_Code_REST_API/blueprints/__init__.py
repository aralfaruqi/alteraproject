import json
from datetime import timedelta
from functools import wraps

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims
from flask_script import Manager

app = Flask(__name__)

app.config['APP_DEBUG'] = True

app.config['JWT_SECRET_KEY'] = 'BGHtgtDYUiLEpecPY78u9UifaM8oSB2hV'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

jwt = JWTManager(app)

def internal_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if not claims['status']:
            return {'status': 'FORBIDDEN', 'message': 'Internal Only!'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/bookstore_database'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.after_request

def after_request(response) :
    if response.status_code == 200 :
        if request.method == 'GET':
            app.logger.info('REQUEST_LOG\t%s',json.dumps({ 'status_code' : response.status_code, 'method' : request.method, 'request' : request.args.to_dict(),'response':json.loads(response.data.decode('utf-8'))}))

        else:
            app.logger.info("REQUEST_LOG\t%s", json.dumps({ 'status_code': response.status_code, 'method' : request.method, 'request' : request.get_json(), 'response': json.loads(response.data.decode('utf-8'))}))
    
    else :
        if request.method == 'GET':
            app.logger.warning('REQUEST_LOG\t%s',json.dumps({ 'status_code' : response.status_code, 'method' : request.method, 'request' : request.args.to_dict(),'response':json.loads(response.data.decode('utf-8'))}))

        else:
            app.logger.warning("REQUEST_LOG\t%s", json.dumps({ 'status_code': response.status_code, 'method' : request.method, 'request' : request.get_json(), 'response': json.loads(response.data.decode('utf-8'))}))
    return response


from blueprints.buku.resources import bp_buku
from blueprints.login import bp_login
from blueprints.penerbit.resources import bp_penerbit

app.register_blueprint(bp_buku, url_prefix='/buku')
app.register_blueprint(bp_login, url_prefix='/login')
app.register_blueprint(bp_penerbit, url_prefix='/penerbit')

db.create_all()
