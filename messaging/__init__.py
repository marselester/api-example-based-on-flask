# coding: utf-8
"""
messaging
~~~~~~~~~

Messaging application.

"""
from flask import Flask
from flask.ext.login import LoginManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.base')
app.config.from_object('config.dev')
app.config.from_pyfile('config.py')

login_manager = LoginManager(app)
login_manager.login_view = 'signin'

from . import views
