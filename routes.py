from endpoints.general.routes import general
from endpoints.users.routes import users
from endpoints.profiles.routes import profiles
from endpoints.trials.routes import trials


def register_endpoints(app):
    app.register_blueprint(users, url_prefix='/api/')
    app.register_blueprint(profiles, url_prefix='/api/')
    app.register_blueprint(trials, url_prefix='/api/')
    app.register_blueprint(general)
