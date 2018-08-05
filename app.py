from flask import Flask
from flask import Flask, flash, jsonify, redirect, Response, render_template, request, session, abort
from access_control import crossdomain
import os
import redis
import datetime
import json


# if os.environ.get("REDIS_URL") != None:
#     server = redis.from_url(os.environ.get("REDIS_URL"))


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcache'
app.config['SECRET_KEY'] = os.urandom(12)

@app.route("/")
@crossdomain("*")
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    """
    HTTP GET
    404 error handler. Returns custom template.
    """
    return Failure.NOT_FOUND_404, 404, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == "__main__":
    app.run()