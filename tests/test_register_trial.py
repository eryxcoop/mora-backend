import unittest
import json

from app import app
from models.collections import ProfilesCollection


class TrialTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.profiles = ProfilesCollection()

    def _url(self):
        return '/api/trials'

    def _a_profile(self, phone_id, profile_name):
        profile_data = {
            "name": profile_name,
            "grade": 3,
            "age": 10,
            "phone_id": phone_id
        }
        self.profiles.add(profile_data)

    def _complete_test_data(self, phone_id=None, profile_name=None):
        phone_id = phone_id or "abc"
        profile_name = profile_name or "abc"

        return {
            "phone_id": phone_id,
            "profile_name": profile_name,
            "system_version": "Android",
            "system_language": "English",
            "app_version": "1",
            "app_language": "Spanish",
            "level": "1 A",
            "operation_type": "1+1",
            "operand_1": 2,
            "operator": "+",
            "operand_2": 3,
            "correct_result": 5,
            "entered_result": 5,
            "correct": True,
            "total_time": 5,
            "start_date": [23, 11, 2020],
            "end_date": [23, 11, 2020],
            "hints_available": False,
            "hints_shown": False,
        }

    def test_if_the_fields_are_correct_and_the_profile_exists_the_trial_is_created(self):
        phone_id = "1"
        profile_name = "Ari"
        self._a_profile(phone_id, profile_name)
        trial_data = self._complete_test_data(phone_id, profile_name)

        # When
        response = self.app.post(self._url(), json=trial_data)

        # Then
        self.assertTrue(json.loads(response.data)['success'])
        self.assertEqual(201, response.status_code)

    def test_if_the_profile_does_not_exist_the_trial_is_not_created(self):
        # Given
        trial_data = self._complete_test_data()

        # When
        response = self.app.post(self._url(), json=trial_data)

        # Then
        self.assertFalse(json.loads(response.data)['success'])
        self.assertEqual(500, response.status_code)