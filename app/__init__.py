from flask import Flask, render_template #, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import form, models



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='404'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', title='500'), 500

# @app.route('/login')
# def login():
#     return render_template('login.html', title='login', class_body='login-body')

@app.route('/set/account')
def account():
    return render_template('account.html', title='account')