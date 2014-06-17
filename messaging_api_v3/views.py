# coding: utf-8
from flask.views import MethodView

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
    },
]
user_list = [
    {
        'name': 'Marsel',
        'access_key': '666',
        'secret_key': 'werxhqb98rpaxn39848xrunpaw3489ruxnpa98w4rxn'
    }
]


@hawk.client_key_loader
def lookup_client_key(client_id):
    for user in user_list:
        if user['access_key'] == client_id:
            return user['secret_key']


class MessageView(MethodView):
    @hawk.verify
    def get(self, message_id):
        return {'get is': 'ok'}

    @hawk.verify
    def post(self):
        return {'post is': 'ok'}

message_view = MessageView.as_view('message')
app.add_url_rule('/messages/', defaults={'message_id': None},
                 view_func=message_view, methods=['GET', ])
app.add_url_rule('/messages/',
                 view_func=message_view, methods=['POST', ])
