# coding: utf-8
"""
messaging_api_v3
~~~~~~~~~~~~~~~~

API version 3.

"""
from api_utils import ResponsiveFlask
from api_utils.auth import Hawk
from messaging import login_manager

app = ResponsiveFlask(__name__, instance_relative_config=True)
app.config.from_object('config.base')
app.config.from_object('config.dev')
app.config.from_pyfile('config.py')

hawk = Hawk(app)
login_manager.init_app(app)

from . import views
