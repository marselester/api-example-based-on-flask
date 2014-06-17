# coding: utf-8
from unittest import TestCase

from werkzeug.test import Client
from werkzeug.wrappers import BaseResponse

from messaging_api import app


class APIVersioningTest(TestCase):

    def setUp(self):
        self.app = Client(app, BaseResponse)

    def test_list_of_messages_by_api_v1_is_available(self):
        r = self.app.get('/v1/messages/')
        expected_status_code = 200

        self.assertEqual(r.status_code, expected_status_code)

    def test_list_of_messages_by_api_v2_is_available(self):
        r = self.app.get('/v2/messages/')
        expected_status_code = 200

        self.assertEqual(r.status_code, expected_status_code)

    def test_404_when_api_version_does_not_exist(self):
        r = self.app.get('/v0/messages/')
        expected_status_code = 404

        self.assertEqual(r.status_code, expected_status_code)
