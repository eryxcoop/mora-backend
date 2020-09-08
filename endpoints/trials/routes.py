from bson.json_util import dumps
from flask import request

from models.collections import TrialsCollection
from utils.login_required import login_required
from . import trials


@trials.route("/trials", methods=["POST"])
@login_required
def register_trial():
    try:
        TrialsCollection().add_many(request.get_json())
        response = {"object": {}, "errors": []}
        status_code = 201
    except Exception as error:
        response = {"object": {}, "errors": [error.message]}
        status_code = 500
    return dumps(response), status_code


@trials.route('/trials', methods=['GET'])
@login_required
def all_trials():
    trials = TrialsCollection().all()
    response = {"object": trials, "errors": []}
    status_code = 200

    return dumps(response), status_code
