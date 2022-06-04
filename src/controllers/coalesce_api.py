from flask import jsonify, make_response, request
from flask_restful import Resource

from src.exceptions.api_exceptions import UserNotFoundError
from src.resources.api_1.api_1 import Api1
from src.resources.api_2.api_2 import Api2
from src.resources.api_3.api_3 import Api3
from src.resources.coalesce.coalesce import Coalesce
from src.resources.coalesce.coalescing_fabric import CoalescingStrategyFabric


class CoalesceApi(Resource):
    def get(self):
        query_string = request.args
        member_id = query_string.get("member_id")
        strategy = CoalescingStrategyFabric.get_strategy(
            query_string.get("coalescing_strategy", "")
        )

        # Retrieving data from external apis
        apis_to_fetch_info_for_coalescing = [Api1, Api2, Api3]

        try:
            dataset_result_list = [
                api(member_id).fetch_info() for api in apis_to_fetch_info_for_coalescing
            ]
        except UserNotFoundError as e:
            return make_response(jsonify({"error": e.__str__()}), 404)

        # Instance Coalesce object
        coalesce = Coalesce(strategy)

        return jsonify(coalesce.execute_coalesce_strategy(dataset_result_list))
