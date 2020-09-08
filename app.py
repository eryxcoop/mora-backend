import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

from database import mongo
from routes import register_endpoints
from settings import Config


def create_app():
    app = Flask(__name__)
    environment_config = Config.for_actual_environment()

    app.config.from_object(environment_config)
    mongo.init_app(app)
    set_up_sentry(environment_config)
    register_endpoints(app)
    return app


def set_up_sentry(environment_config):
    if environment_config.should_handle_errors():
        sentry_sdk.init(
            dsn="https://310afe568f4843609c1a65ca8d95a4e7@o73280.ingest.sentry.io/5420577",
            integrations=[FlaskIntegration()],
            traces_sample_rate=1.0,
            environment=environment_config.name()
        )


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
