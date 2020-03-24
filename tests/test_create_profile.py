import unittest
import json

from app import app


class ProfileTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def _url(self):
        return '/api/profiles'

    def test_if_the_fields_are_correct_the_profile_is_created(self):
        # Given
        profile_data = {
            "name": "Maxi",
            "grade": 3,
            "age": 10,
            "phone_id": "abc"
        }

        # When
        response = self.app.post(self._url(), json=profile_data)

        # Then
        self.assertTrue(json.loads(response.data)['success'])
        self.assertEqual(201, response.status_code)

    def test_if_a_field_is_missing_the_profile_is_not_created(self):
        # Given
        profile_data = {
            "name": "Maxi",
            "age": 10,
            "phone_id": "abc"
        }

        # When
        response = self.app.post(self._url(), json=profile_data)

        # Then
        self.assertFalse(json.loads(response.data)['success'])
        self.assertIn("grade", json.loads(response.data)['error_message'])
        self.assertEqual(500, response.status_code)

    def test_if_a_fields_type_is_wrong_the_profile_is_not_created(self):
        # Given
        profile_data = {
            "name": "Maxi",
            "age": 10,
            "phone_id": "abc",
            "grade": "3"
        }

        # When
        response = self.app.post(self._url(), json=profile_data)

        # Then
        self.assertFalse(json.loads(response.data)['success'])
        self.assertIn("3", json.loads(response.data)['error_message'])
        self.assertEqual(500, response.status_code)

    def test_if_theres_an_additional_field_the_profile_is_not_created(self):
        # Given
        profile_data = {
            "name": "Maxi",
            "age": 10,
            "phone_id": "abc",
            "grade": 3,
            "additional_field": "3",
        }

        # When
        response = self.app.post(self._url(), json=profile_data)

        # Then
        self.assertFalse(json.loads(response.data)['success'])
        self.assertIn("additional_field", json.loads(response.data)['error_message'])
        self.assertEqual(500, response.status_code)
