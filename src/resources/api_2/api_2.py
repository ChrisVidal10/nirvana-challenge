from typing import Dict

from flask import current_app

from src.exceptions.api_exceptions import UserNotFoundError
from src.resources.base_external_api import BaseExtApi
from src.resources.base_external_interface import BaseExternalApiInterface


class Api2(BaseExtApi, BaseExternalApiInterface):
    # Sample Database Implementation for Api #2
    _DB = {
        "1": {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000},
        "2": {"deductible": 2400, "stop_loss": 26000, "oop_max": 12000},
        "3": {"deductible": 3600, "stop_loss": 39000, "oop_max": 18000},
        "4": {"deductible": 4800, "stop_loss": 52000, "oop_max": 24000},
    }

    def __init__(self, member_id: str):
        super().__init__(member_id)

    def fetch_info(self) -> Dict[str, int]:

        # In this method would be necessary to implement a call to a real API_2
        # For take home project purposes a mock value will be returned
        try:
            result = self._DB[self.member_id]
        except KeyError as e:
            current_app.logger.info("User not found")
            raise UserNotFoundError(self.member_id)

        return result
