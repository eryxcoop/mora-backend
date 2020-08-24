from bson.json_util import dumps
from flask import request

from models.collections import ProfilesCollection
from . import profiles


@profiles.route('/profile', methods=['POST'])
def create_profile():
    try:
        ProfilesCollection().add(request.get_json())
        response = {"object": {}, "errors": []}
        status_code = 201
    except Exception as error:
        response = {"object": {}, "errors": [error.message]}
        status_code = 500
    return dumps(response), status_code


@profiles.route('/profiles', methods=['POST'])
def create_profiles():
    try:
        ProfilesCollection().add_many(request.get_json())
        response = {"object": {}, "errors": []}
        status_code = 201
    except Exception as error:
        response = {"object": {}, "errors": [error.message]}
        status_code = 500
    return dumps(response), status_code


@profiles.route('/profiles', methods=['GET'])
def all_profiles():
    profiles = ProfilesCollection().all()
    response = {"object": profiles, "errors": []}
    status_code = 200

    return dumps(response), status_code
