from bson.json_util import dumps
from flask import request

from models.collections import TrialsCollection
from . import trials


@trials.route("/trials", methods=["POST"])
def register_trial():
    try:
        TrialsCollection().add(request.get_json())
        response = {"success": True}
        status_code = 201
    except Exception as error:
        response = {"success": False, "error_message": error.message}
        status_code = 500
    return dumps(response), status_code
