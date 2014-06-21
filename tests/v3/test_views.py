# coding: utf-8
import json
from unittest import TestCase

import mohawk

from messaging_api_v3 import app


class AuthTest(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hawk_method_get(self):
        data = {}
        credentials = {
            'id': '666',
            'key': 'werxhqb98rpaxn39848xrunpaw3489ruxnpa98w4rxn',
            'algorithm': 'sha256'
        }
        url = 'http://localhost/messages/?hello=world'
        method = 'GET'
        content = json.dumps(data)
        content_type = 'application/json'

        sender = mohawk.Sender(
            credentials,
            url,
            method,
            content,
            content_type
        )

        r = self.app.get(
            '/messages/',
            headers={
                'Authorization': sender.request_header
            },
            query_string={
                'hello': 'world'
            },
            data=content,
            content_type=content_type
        )
        expected_status_code = 200
        self.assertEqual(r.status_code, expected_status_code)

    def test_hawk_method_post(self):
        data = {
            'fizz': 'buzz',
            'blah': '1111'
        }
        credentials = {
            'id': '666',
            'key': 'werxhqb98rpaxn39848xrunpaw3489ruxnpa98w4rxn',
            'algorithm': 'sha256'
        }
        url = 'http://localhost/messages/?hello=world'
        method = 'POST'
        content = json.dumps(data)
        content_type = 'application/json'

        sender = mohawk.Sender(
            credentials,
            url,
            method,
            content,
            content_type
        )

        r = self.app.post(
            '/messages/',
            headers={
                'Authorization': sender.request_header
            },
            query_string={
                'hello': 'world'
            },
            data=content,
            content_type=content_type
        )
        expected_status_code = 200
        self.assertEqual(r.status_code, expected_status_code)
