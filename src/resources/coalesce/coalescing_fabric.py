from typing import Type

from src.resources.coalesce.strategies.max_strategy import MaxStrategy
from src.resources.coalesce.strategies.mean_strategy import MeanStrategy
from src.resources.coalesce.strategies.median_strategy import MedianStrategy
from src.resources.coalesce.strategies.min_strategy import MinStrategy
from src.resources.coalesce.strategies.mode_strategy import ModeStrategy
from src.resources.coalesce.strategies.strategy_interface import \
    StrategyInterface


class CoalescingStrategyFabric:

    _STRATEGIES = {
        "mean": MeanStrategy,
        "mode": ModeStrategy,
        "median": MedianStrategy,
        "max": MaxStrategy,
        "min": MinStrategy,
    }

    @classmethod
    def get_strategy(cls, strategy: str) -> StrategyInterface:
        """
        Fabric of coalescing strategies
        :param strategy: Strategy name
        :return: Return an instance of a strategy.
        If the strategy is not implemented, a Mean Strategy instance is return
        """
        return cls._STRATEGIES.get(strategy.lower(), MeanStrategy)()
