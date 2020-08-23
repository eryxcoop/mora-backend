import unittest
import json
from database import mongo

from app import app
from models.collections import ProfilesCollection


class ProfileTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = mongo.db

    def _url(self):
        return '/api/profiles'

    def test_if_the_fields_are_correct_the_profile_is_created(self):
        # Given
        profile_data = {
            "name": "Maxi",
            "avatarName": "eternauta",
            "age": 10,
            "phoneId": "abc"
        }

        # When
        response = self.app.post(self._url(), json=profile_data)

        # Then
        self.assertEqual(201, response.status_code)
        self.assertFalse(json.loads(response.data)['errors'])

    def test_if_a_field_is_missing_the_profile_is_not_created(self):
        # Given
        profile_data = {
            "name": "Maxi",
            "age": 10,
            "phoneId": "abc"
        }

        # When
        response = self.app.post(self._url(), json=profile_data)

        # Then
        self.assertEqual(500, response.status_code)
        self.assertTrue(json.loads(response.data)['errors'])
        self.assertIn(ProfilesCollection.AVATAR_NAME_FIELD, json.loads(response.data)['errors'][0])

    def test_if_a_fields_type_is_wrong_the_profile_is_not_created(self):
        # Given
        invalid_avatar_name = 3
        profile_data = {
            "name": "Maxi",
            "age": 10,
            "phoneId": "abc",
            "avatarName": invalid_avatar_name
        }

        # When
        response = self.app.post(self._url(), json=profile_data)

        # Then
        self.assertEqual(500, response.status_code)
        self.assertTrue(json.loads(response.data)['errors'])
        self.assertIn(str(invalid_avatar_name), json.loads(response.data)['errors'][0])

    def test_if_theres_an_additional_field_the_profile_is_not_created(self):
        # Given
        profile_data = {
            "name": "Maxi",
            "age": 10,
            "phoneId": "abc",
            "avatarName": "un avatar",
            "additionalField": "3",
        }

        # When
        response = self.app.post(self._url(), json=profile_data)

        # Then
        self.assertEqual(500, response.status_code)
        self.assertTrue(json.loads(response.data)['errors'])
        self.assertIn("additionalField", json.loads(response.data)['errors'][0])

    def tearDown(self):
        # Delete Database collections after the test is complete
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
