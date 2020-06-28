from database import mongo
from jsonschema import validate, ValidationError


class ProfilesCollection(object):
    def __init__(self, ):
        self._profiles = mongo.db.profiles_list

    def _validate(self, json_data):
        validate(instance=json_data, schema=self._json_schema())

    def add(self, json_data):
        self._validate(json_data)
        self._profiles.insert_one(json_data)

    def all(self):
        return self._profiles.find()

    def exists_with(self, phone_id, name):
        return self._profiles.count_documents({"name": name, "phone_id": phone_id}) != 0

    def _json_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "number"},
                "phone_id": {"type": "string"},
                "avatar_name": {"type": "string"}
            },
            "required": ["name", "age", "phone_id", "avatar_name"],
            "additionalProperties": False
        }
        return schema


class TrialsCollection(object):
    def __init__(self,):
        self._trials = mongo.db.trials_list

    def add(self, json_data):
        self._validate(json_data)
        self._trials.insert_one(json_data)

    def add_many(self, trials):
        for trial in trials:
            self._validate(trial)

        self._trials.insert_many(trials)

    def all(self):
        return self._trials.find()

    def _validate(self, json_data):
        validate(instance=json_data, schema=self._json_schema())
        self._validate_profile_data(json_data["phoneId"], json_data["profileName"])

    def _validate_profile_data(self, phone_id, profile_name):
        profiles = ProfilesCollection()
        if not profiles.exists_with(phone_id=phone_id, name=profile_name):
            raise ValidationError("A profile for that phone id and name does not exist.")

    def _json_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "phoneId": {"type": "string"},
                "profileName": {"type": "string"},
                "systemLanguage": {"type": "string"},
                "appVersion": {"type": "string"},
                "appLanguage": {"type": "string"},
                "planet": {"type": "number"},
                "mission": {"type": "number"},
                "episode": {"type": "number"},
                "question": {"type": "string"},
                "correctAnswer": {"type": "number"},
                "options": {"type": "array"},
                "userAnswer": {"type": "number"},
                "startTime": {"type": "number"},
                "endTime": {"type": "number"}
            },
            "required": ["phoneId", "profileName", "planet", "mission", "episode", "question", "correctAnswer",
                         "options", "userAnswer", "startTime", "endTime"],
            "additionalProperties": False
        }
        return schema
