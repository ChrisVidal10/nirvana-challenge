from typing import Dict

from flask import current_app

from src.exceptions.api_exceptions import UserNotFoundError
from src.resources.base_external_api import BaseExtApi
from src.resources.base_external_interface import BaseExternalApiInterface


class Api3(BaseExtApi, BaseExternalApiInterface):
    # Sample Database Implementation for Api #3
    _DB = {
        "1": {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000},
        "2": {"deductible": 2000, "stop_loss": 20000, "oop_max": 12000},
        "3": {"deductible": 3000, "stop_loss": 30000, "oop_max": 18000},
        "4": {"deductible": 4000, "stop_loss": 40000, "oop_max": 24000},
    }

    def __init__(self, member_id: str):
        super().__init__(member_id)

    def fetch_info(self) -> Dict[str, int]:

        # In this method would be necessary to implement a call to a real API_3
        # For take home project purposes a mock value will be returned
        try:
            result = self._DB[self.member_id]
        except KeyError as e:
            current_app.logger.info("User not found")
            raise UserNotFoundError(self.member_id)

        return result
