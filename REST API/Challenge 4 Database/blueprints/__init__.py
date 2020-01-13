import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)

app.config['APP_DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/client_database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)
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

from blueprints.client.resources import bp_client
app.register_blueprint(bp_client, url_prefix='/client')

from blueprints.book.resources import bp_book
app.register_blueprint(bp_book, url_prefix='/book')

from blueprints.user.resources import bp_user
app.register_blueprint(bp_user, url_prefix='/user')

from blueprints.rent.resources import bp_rent
app.register_blueprint(bp_rent, url_prefix='/rent')

db.create_all()

