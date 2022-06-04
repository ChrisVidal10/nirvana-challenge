from flask_restful import Api

from src.controllers.coalesce_api import CoalesceApi


def initialize_routes(api: Api) -> None:
    api.add_resource(CoalesceApi, "/coalesce-api")
