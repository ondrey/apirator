# -*- coding: utf-8 -*-


from flask import Flask
from flask import render_template
from flask import abort

import api

from datetime import timedelta


app = Flask(__name__)
@app.route('/<api_group>/<method_api>', methods=["GET", "POST"])
def run_api_method(api_group, method_api):

    if api_group in api.__dict__:
        obj = api.__dict__[api_group]()
        return obj.run_api_method(method_api)
    abort(404)


@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

app.config.from_object('config.DevelopmentConfig')

app.run()
