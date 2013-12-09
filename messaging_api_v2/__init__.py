# coding: utf-8
"""
messaging_api_v2
~~~~~~~~~~~~~~~~

API version 2.

"""
from flask import Flask

app = Flask(__name__)
app.debug = True

from . import views
