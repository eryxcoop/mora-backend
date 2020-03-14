from bson.json_util import dumps
from jsonschema import validate

from database import mongo
from flask import request
from . import profiles


def define_json_schema():
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


def json_is_valid(json):
    try:
        validate(instance=json, schema=define_json_schema())
        return True, ""
    except Exception as e:
        return False, e.message


@profiles.route('/profiles', methods=['POST'])
def create_profile():
    data = request.get_json()

    is_valid, error_message = json_is_valid(data)
    if is_valid:
        mongo.db.profiles_list.insert_one(data)
        response = {"success": True}
    else:
        response = {"success": False, "error_message": "Incorrect fields - %s" % error_message}

    return dumps(response)
