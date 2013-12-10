# coding: utf-8
from unittest import TestCase

from messaging_api_v2 import app


class MessageViewTest(TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_200_json_response_after_get_request(self):
        r = self.app.get('/messages/')
        expected_status_code = 200

        self.assertEqual(r.status_code, expected_status_code)
        self.assertEqual(r.mimetype, 'application/json')

    def test_201_json_response_after_post_response(self):
        r = self.app.post('/messages/')
        expected_status_code = 201

        self.assertEqual(r.status_code, expected_status_code)
        self.assertEqual(r.mimetype, 'application/json')

    def test_400_json_response_after_put_response(self):
        r = self.app.put('/messages/1')
        expected_status_code = 400

        self.assertEqual(r.status_code, expected_status_code)
        self.assertEqual(r.mimetype, 'application/json')
