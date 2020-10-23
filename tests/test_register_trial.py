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
            "avatarName": "avatar",
            "age": 10,
            "phoneId": phone_id,
            "gender": "M",
            "grade": "septimo"
        }
        self.profiles.add(profile_data)

    def _mocked_trials_for(self, phone_id=None, profile_name=None):
        phone_id = phone_id or "abc"
        profile_name = profile_name or "abc"

        return [{
            "phoneId": phone_id,
            "profileName": profile_name,
            "planet": 1,
            "mission": 1,
            "episode": 1,
            "question": "1+1",
            "correctAnswer": 2,
            "options": [1, 2, 3, 4],
            "userAnswer": 4,
            "startTime": 1234123,
            "endTime": 1234123,
        }]

    def test_if_the_fields_are_correct_and_the_profile_exists_the_trial_is_created(self):
        phone_id = "1"
        profile_name = "Ari"
        self._a_profile(phone_id, profile_name)
        trial_data = self._mocked_trials_for(phone_id, profile_name)

        # When
        response = self.app.post(self._url(), json=trial_data)

        # Then
        self.assertEqual(201, response.status_code)
        self.assertFalse(json.loads(response.data)['errors'])

    def test_if_the_profile_does_not_exist_the_trial_is_not_created(self):
        # Given
        trial_data = self._mocked_trials_for()

        # When
        response = self.app.post(self._url(), json=trial_data)

        # Then
        self.assertTrue(json.loads(response.data)['errors'])
        self.assertEqual(500, response.status_code)
