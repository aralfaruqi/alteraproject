from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json,logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)
api = Api(app, catch_all_404s=True)

from blueprints.client.resources import bp_client

app.register_blueprint(bp_client, url_prefix ='/client')

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

if __name__ == '__main__':
    formatter = logging.Formatter("[%(asctime)s]{%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

    log_handler = RotatingFileHandler("%s%s" % (app.root_path, '/storage/log/app.log'),maxBytes=100000, backupCount=10)
    # log_handler.setLevel(logging.INFO)
    logging.getLogger().setLevel('INFO')
    log_handler.setFormatter(formatter)
    app.logger.addHandler(log_handler)
    app.run(debug=True, host='0.0.0.0', port=5000)

