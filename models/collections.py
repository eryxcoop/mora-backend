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

    def exists_with(self, phone_id, name):
        return self._profiles.count_documents({"name": name, "phone_id": phone_id}) != 0

    def _json_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "number"},
                "grade": {"type": "number"},
                "phone_id": {"type": "string"},
            },
            "required": ["name", "age", "grade", "phone_id"],
            "additionalProperties": False
        }
        return schema


class TrialsCollection(object):
    def __init__(self,):
        self._trials = mongo.db.trials_list

    def add(self, json_data):
        self._validate(json_data)
        self._trials.insert_one(json_data)

    def _validate(self, json_data):
        validate(instance=json_data, schema=self._json_schema())
        self._validate_profile_data(json_data["phone_id"], json_data["profile_name"])

    def _validate_profile_data(self, phone_id, profile_name):
        profiles = ProfilesCollection()
        if not profiles.exists_with(phone_id=phone_id, name=profile_name):
            raise ValidationError("A profile for that phone id and name does not exist.")

    def _json_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "phone_id": {"type": "string"},
                "profile_name": {"type": "string"},
                "system_version": {"type": "string"},
                "system_language": {"type": "string"},
                "app_version": {"type": "string"},
                "app_language": {"type": "string"},
                "level": {"type": "string"},
                "operation_type": {"type": "string"},
                "operand_1": {"type": "number"},
                "operator": {"type": "string"},
                "operand_2": {"type": "number"},
                "correct_result": {"type": "number"},
                "entered_result": {"type": "number"},
                "correct": {"type": "boolean"},
                "total_time": {"type": "number"},
                "start_date": {"type": "array"},
                "end_date": {"type": "array"},
                "hints_available": {"type": "boolean"},
                "hints_shown": {"type": "boolean"},
            },
            "required": ["phone_id", "profile_name", "system_version", "system_language",
                         "app_version", "app_language", "level", "operation_type",
                         "operand_1", "operator", "operand_2", "correct_result", "entered_result",
                         "correct", "total_time", "start_date", "end_date", "hints_available",
                         "hints_shown"],
            "additionalProperties": False
        }
        return schema