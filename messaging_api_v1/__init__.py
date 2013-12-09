# coding: utf-8
"""
messaging_api_v1
~~~~~~~~~~~~~~~~

API version 1.

"""
from flask import Flask

app = Flask(__name__)
app.debug = True

from . import views
