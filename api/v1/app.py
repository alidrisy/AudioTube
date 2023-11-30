#!/usr/bin/python3
""" Flask API for AudioTube Application """
from flask import Flask, jsonify, make_response
from api.v1.views import app_audio
from flask_cors import CORS
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_audio)
CORS(app, resources={r"/api/v1/*": {"origin": "*"}})


@app.errorhandler(404)
def not_found(error):
    """ Handel error 404 """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    app.run(host=getenv('AY_HOST', '0.0.0.0'), port=getenv('AY_PORT', 5001))
