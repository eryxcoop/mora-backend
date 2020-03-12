from bson.json_util import dumps

from database import mongo
from flask import request
from . import profiles


def has_required_fields(data):
    required_fields = ["name", "age", "alias", "grade", "phone_id"]
    return all(field in data for field in required_fields)


def name_is_valid(data):
    number_of_profiles_with_the_same_name_for_phone = mongo.db.profiles_list.count_documents(
        {"phone_id": data["phone_id"], "name": data["name"]})
    return number_of_profiles_with_the_same_name_for_phone > 0


@profiles.route('/profiles', methods=['POST'])
def create_profile():
    data = request.get_json()

    if not has_required_fields(data):
        response = {"success": False, "message": "Fields missing"}
    elif not name_is_valid(data):
        response = {"success": False, "message": "A profile with the same name is associated with the phone"}
    else:
        mongo.db.profiles_list.insert_one(data)
        response = mongo.db.profiles_list.find_one()
        response.update({"success": True})

    return dumps(response)
