import abc
from typing import Dict, List


class StrategyInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self, datasets: List[Dict[str, int]]):
        raise NotImplementedError
