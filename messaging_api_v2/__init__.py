# coding: utf-8
"""
messaging_api_v2
~~~~~~~~~~~~~~~~

API version 2.

"""
from api_utils import ResponsiveFlask

app = ResponsiveFlask(__name__)
app.debug = True

from . import views
