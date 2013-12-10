# coding: utf-8
from flask import request
from flask.views import MethodView

from . import app


message_list = [
    {
        'content': 'hello world from V2',
    },
    {
        'content': 'hi world from V2',
    },
]


class MessageView(MethodView):

    def get(self, message_id):
        """Shows list of messages or certain message if id is given."""
        if message_id is None:
            return {'messages': message_list}
        return message_list[message_id]

    def post(self):
        """Creates message."""
        return {}, 201, {'Location': '/messages/<new_id>'}

    def put(self, message_id):
        """Updates message."""
        # reproduce key error
        request.args['blah']

    def delete(self, message_id):
        """Deletes message."""
        return {}

message_view = MessageView.as_view('message')
app.add_url_rule('/messages/', defaults={'message_id': None},
                 view_func=message_view, methods=['GET', ])
app.add_url_rule('/messages/',
                 view_func=message_view, methods=['POST', ])
app.add_url_rule('/messages/<int:message_id>',
                 view_func=message_view, methods=['GET', 'PUT', 'DELETE'])
