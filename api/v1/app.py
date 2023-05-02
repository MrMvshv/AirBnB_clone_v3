#!/usr/bin/python3
""" Main entry point of flask app"""

import os
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    apiHost = os.environ.get('HBNB_API_HOST')
    if apiHost is None:
        apiHost = '0.0.0.0'
    apiPort = os.environ.get('HBNB_API_PORT')
    if apiPort is None:
        apiPort = '5000'

    app.run(host=apiHost, port=apiPort, threaded=True)
