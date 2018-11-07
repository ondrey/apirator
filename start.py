# -*- coding: utf-8 -*-


from flask import Flask
from flask import render_template
from flask import abort

import LibAPI

from datetime import timedelta


app = Flask(__name__)
@app.route('/<api_group>/<method_api>', methods=["GET", "POST"])
def run_api_method(api_group, method_api):

    if api_group in LibAPI.__dict__:
        obj = LibAPI.__dict__[api_group]()
        return obj.run_api_method(method_api)
    abort(404)


@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#Зададим время жизни сессии
app.permanent_session_lifetime = timedelta(minutes=120)
# Создадим секретный ключ для сессии.
app.secret_key = '\x00\xf1\x00Bv\x97\x97K\x11w\xd0vJ\xcfL\xf2\xcf\x90\\1\x04\xe1\xe3g'


app.run(debug=True)