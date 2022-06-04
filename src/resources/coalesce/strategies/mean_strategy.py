import statistics
from math import floor
from typing import Dict, List

from src.resources.coalesce.strategies.strategies_utils import StrategiesUtils
from src.resources.coalesce.strategies.strategy_interface import \
    StrategyInterface


class MeanStrategy(StrategyInterface):
    def execute(self, datasets: List[Dict[str, int]]):
        datasets_grouped_by_keys = StrategiesUtils.group_by_key(datasets)
        return {
            key: floor(statistics.mean(value_list))
            for key, value_list in datasets_grouped_by_keys.items()
        }
