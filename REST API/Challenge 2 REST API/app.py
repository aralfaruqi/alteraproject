from flask import Flask, request
import json
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

from blueprints.client.resources import bp_client

app.register_blueprint(bp_client, url_prefix ='/client')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
