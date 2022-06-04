from typing import Dict, List

from src.resources.coalesce.strategies.strategies_utils import StrategiesUtils
from src.resources.coalesce.strategies.strategy_interface import \
    StrategyInterface


class MinStrategy(StrategyInterface):
    def execute(self, datasets: List[Dict[str, int]]):
        datasets_grouped_by_keys = StrategiesUtils.group_by_key(datasets)
        return {
            key: min(value_list) for key, value_list in datasets_grouped_by_keys.items()
        }
