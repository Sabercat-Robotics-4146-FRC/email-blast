from flask import Flask
from flask import Flask, flash, jsonify, redirect, Response, render_template, request, session, abort
from access_control import crossdomain
import os
import redis
import datetime
import json
from Mailer import mass_email


# if os.environ.get("REDIS_URL") != None:
#     server = redis.from_url(os.environ.get("REDIS_URL"))


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcache'
app.config['SECRET_KEY'] = os.urandom(12)

@app.route('/', methods=['GET', 'POST'])
@crossdomain("*")
def index():
    if request.method == 'POST':
        password = request.form['password']
        body = request.form['body']
        subject = request.form['subject']
        heading = request.form['heading']
        mail_list = request.form['emails']
        if not password or not body or not subject or not heading or not mail_list:
            return render_template('index.html', error="Make sure you have all the fields filled out.")
        mail_list = mail_list.split(",")
        try:
            mass_email(subject, heading, body, password, mail_list)
        except Exception as inst:
            return render_template('index.html', error="Internal Server Error: " + str(inst) )

        return render_template('index.html', success="Email Sent!")
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == "__main__":
    app.run()