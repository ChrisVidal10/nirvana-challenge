from flask import jsonify, request, make_response
from flask_restful import Resource


class CoalesceApi(Resource):

    def get(self):
        return jsonify({"deductible": 1066, "stop_loss": 11000, "oop_max": 5666})