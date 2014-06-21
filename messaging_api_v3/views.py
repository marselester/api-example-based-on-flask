# coding: utf-8
from flask.views import MethodView

from messaging.models import user_list
from . import app, hawk

message_list = [
    {
        'content': 'hello world from V2',
        'is_deleted': False,
    },
    {
        'content': 'hi world from V2',
        'is_deleted': False,
    },
    {
        'content': 'I was deleted',
        'is_deleted': True,
    }
]


@app.default_errorhandler
def http_error_handler(error):
    response = {
        'code': error.code,
        'message': str(error),
    }
    return response, error.code


@hawk.client_key_loader
def lookup_client_key(client_id):
    for user in user_list:
        if user.access_key == client_id:
            return user.secret_key
    else:
        raise LookupError()


class MessageView(MethodView):
    decorators = [hawk.auth_required]

    def get(self, message_id):
        return {'get is': 'ok'}

    def post(self):
        return {'post is': 'ok'}

message_view = MessageView.as_view('message')
app.add_url_rule('/messages/', defaults={'message_id': None},
                 view_func=message_view, methods=['GET', ])
app.add_url_rule('/messages/',
                 view_func=message_view, methods=['POST', ])
