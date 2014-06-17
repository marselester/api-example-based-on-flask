# coding: utf-8
"""
messaging_api_v3
~~~~~~~~~~~~~~~~

API version 3.

"""
from api_utils import ResponsiveFlask
from api_utils.auth import Hawk

app = ResponsiveFlask(__name__)

hawk = Hawk(app)

from . import views
