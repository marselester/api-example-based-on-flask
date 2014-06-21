# coding: utf-8
from flask import request, abort
from flask.views import MethodView

from . import app

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


class MessageView(MethodView):
    def get(self, message_id):
        """Shows list of active messages or certain message if id is given.

        If requested message is deleted it should return 410.

        """
        if message_id is None:
            return {
                'messages': [m for m in message_list if not m['is_deleted']]
            }

        try:
            message = message_list[message_id]
        except IndexError:
            abort(404)

        if message['is_deleted']:
            return {}, 410
        else:
            return message

    def post(self):
        """Creates message."""
        return {}, 201, {'Location': '/messages/<new_id>'}

    def put(self, message_id):
        """Updates message.

        If data is not changed it should return 304.

        """
        # reproduce key error
        request.args['blah']

    def delete(self, message_id):
        """Deletes message."""
        return {}, 204

message_view = MessageView.as_view('message')
app.add_url_rule('/messages/', defaults={'message_id': None},
                 view_func=message_view, methods=['GET', ])
app.add_url_rule('/messages/',
                 view_func=message_view, methods=['POST', ])
app.add_url_rule('/messages/<int:message_id>',
                 view_func=message_view, methods=['GET', 'PUT', 'DELETE'])
