from endpoints.users.routes import users


def register_endpoints(app):
    app.register_blueprint(users, url_prefix='/api/')
