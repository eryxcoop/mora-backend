from flask import render_template

from . import general


@general.route('/privacy-policy', methods=['GET'])
def privacy_policy():
    return render_template("privacy-policy.html")
