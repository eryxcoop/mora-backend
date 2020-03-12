from database import mongo
from . import trials


@trials.route("/trials", methods=["GET"])
def register_trial():
    pass