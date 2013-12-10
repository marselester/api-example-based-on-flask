# coding: utf-8
from unittest import TestCase

from messaging_api_v1 import app


class UrlNamingTest(TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_301_if_plural_noun_does_not_end_with_slash(self):
        r = self.app.get('/messages')
        expected_status_code = 301

        self.assertEqual(r.status_code, expected_status_code)

    def test_404_if_resource_ends_with_slash(self):
        r = self.app.get('/messages/1/')
        expected_status_code = 404

        self.assertEqual(r.status_code, expected_status_code)

    def test_get_from_plural_noun_that_ends_with_slash(self):
        r = self.app.get('/messages/')
        expected_status_code = 200

        self.assertEqual(r.status_code, expected_status_code)

    def test_post_to_plural_noun_that_ends_with_slash(self):
        r = self.app.post('/messages/')
        expected_status_code = 200

        self.assertEqual(r.status_code, expected_status_code)

    def test_put_to_plural_noun_is_not_allowed(self):
        r = self.app.put('/messages/')
        expected_status_code = 405

        self.assertEqual(r.status_code, expected_status_code)

    def test_delete_plural_noun_is_not_allowed(self):
        r = self.app.delete('/messages/')
        expected_status_code = 405

        self.assertEqual(r.status_code, expected_status_code)

    def test_get_message_by_id_that_has_no_slash(self):
        r = self.app.get('/messages/1')
        expected_status_code = 200

        self.assertEqual(r.status_code, expected_status_code)

    def test_post_message_by_id_is_not_allowed(self):
        r = self.app.post('/messages/1')
        expected_status_code = 405

        self.assertEqual(r.status_code, expected_status_code)

    def test_update_message_by_id_that_has_no_slash(self):
        r = self.app.put('/messages/1')
        expected_status_code = 200

        self.assertEqual(r.status_code, expected_status_code)

    def test_delete_message_by_id_that_has_no_slash(self):
        r = self.app.delete('/messages/1')
        expected_status_code = 200

        self.assertEqual(r.status_code, expected_status_code)
