from functools import wraps
import json
from flask import request

from settings import Config

EXEMPT_METHODS = {'OPTIONS'}


def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in EXEMPT_METHODS:
            return func(*args, **kwargs)

        environment_config = Config.for_actual_environment()
        if not environment_config.need_authorization():
            return func(*args, **kwargs)

        token = request.headers.get('Authorization')
        if token != environment_config.token():
            return json.dumps({"object": {}, "errors": ["Ingreso no permitido"]}), 403

        return func(*args, **kwargs)

    return decorated_view
