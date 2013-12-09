# coding: utf-8
"""
messaging_api
~~~~~~~~~~~~~

It is API version dispatcher of Internal Messaging System.

Each WSGI application is bound to version url.

"""
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.exceptions import NotFound

import messaging_api_v1
import messaging_api_v2


app = DispatcherMiddleware(NotFound(), {
    '/v1': messaging_api_v1.app,
    '/v2': messaging_api_v2.app,
})
