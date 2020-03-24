from bson.json_util import dumps
from flask import request

from models.collections import ProfilesCollection
from . import profiles


@profiles.route('/profiles', methods=['POST'])
def create_profile():
    try:
        ProfilesCollection().add(request.get_json())
        response = {"success": True}
        status_code = 201
    except Exception as error:
        response = {"success": False, "error_message": error.message}
        status_code = 500
    return dumps(response), status_code
