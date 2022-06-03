from flask_restful import Api
from resources.coalesce_api import CoalesceApi


def initialize_routes(api: Api) -> None:
    api.add_resource(CoalesceApi, '/coalesce-api')
