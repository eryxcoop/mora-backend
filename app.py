from flask import Flask
from routes import register_endpoints
from settings import Config
from database import mongo


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config.for_actual_environment())
    mongo.init_app(app)
    register_endpoints(app)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
