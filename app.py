import os
from flask import Flask, Request, jsonify, Response
import json
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("Request Successful")
    return "Hello World!"

@app.route("/status")
def status():
    response = json.dumps({"result": " OK - healthy"})
    app.logger.info("Request Successful")
    return response

@app.route("/metrics")
def metric():
    app.logger.info(" Request Successful")
    return json.dumps({"data":{"UserCount": 140, "UserCountActive": 23}})
if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
