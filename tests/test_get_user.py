import unittest
import json

from app import app
from database import mongo


class ExampleTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = mongo.db

    def test_example(self):
        # Given

        # When
        response = self.app.get('/api/users', headers={"Content-Type": "application/json"})

        # Then
        self.assertEqual("usuarioDeTest", json.loads(response.data)['juan'])
        self.assertEqual(200, response.status_code)

