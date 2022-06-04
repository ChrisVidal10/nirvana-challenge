from flask import Flask
from flask_restful import Api

from src.controllers.routes import initialize_routes


def create_app(config_filename=None) -> Flask:
    """
    Application Factory Function
    :param config_filename: A config file to instance a flask app.
    :return:
    """

    # Init app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    # Init flask restful
    api = Api(app)

    # Init controllers endpoints
    initialize_routes(api)

    return app
