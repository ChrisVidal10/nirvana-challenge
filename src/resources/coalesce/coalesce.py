from typing import Dict, List, Type

from src.resources.coalesce.strategies.strategy_interface import \
    StrategyInterface


class Coalesce:
    def __init__(self, strategy: StrategyInterface):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: StrategyInterface):
        self._strategy = strategy

    def execute_coalesce_strategy(self, datasets: List[Dict[str, int]]):
        return self._strategy.execute(datasets)
