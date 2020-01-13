from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims
import json
from datetime import timedelta
from functools import wraps


app = Flask(__name__)

app.config['APP_DEBUG'] = True
app.config['JWT_SECRET_KEY'] = 'fjtkigk87kvmsdiMDni7632jk3lNeurt'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)

jwt = JWTManager(app)


def internal_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['status'] != 'super_user':
            return {'status' : 'FORBIDDEN', 'message' : 'Internal Only!'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/db_challenge6'
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


from blueprints.book.resource import bp_book
app.register_blueprint(bp_book, url_prefix = '/book')

from blueprints.client.resource import bp_client
app.register_blueprint(bp_client, url_prefix = '/client')

from blueprints.user.resource import bp_user
app.register_blueprint(bp_user, url_prefix = '/user')

from blueprints.rent.resource import bp_rent
app.register_blueprint(bp_rent, url_prefix = '/rent')

from blueprints.auth import bp_auth
app.register_blueprint(bp_auth, url_prefix='/auth')

from blueprints.weather.resource import bp_weather
app.register_blueprint(bp_auth, url_prefix='/weather')

db.create_all()