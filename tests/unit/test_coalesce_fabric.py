import pytest

from src.resources.coalesce.coalescing_fabric import CoalescingStrategyFabric
from src.resources.coalesce.strategies.max_strategy import MaxStrategy
from src.resources.coalesce.strategies.mean_strategy import MeanStrategy
from src.resources.coalesce.strategies.median_strategy import MedianStrategy
from src.resources.coalesce.strategies.min_strategy import MinStrategy
from src.resources.coalesce.strategies.mode_strategy import ModeStrategy


@pytest.mark.parametrize(
    "mock_coalescing_strategy, expected_instanced_strategy",
    [
        ("", MeanStrategy),
        ("mean", MeanStrategy),
        ("MEAN", MeanStrategy),
        ("mEaN", MeanStrategy),
        ("median", MedianStrategy),
        ("MEDIAN", MedianStrategy),
        ("mEdIan", MedianStrategy),
        ("mode", ModeStrategy),
        ("MODE", ModeStrategy),
        ("mOdE", ModeStrategy),
        ("max", MaxStrategy),
        ("MAX", MaxStrategy),
        ("mAx", MaxStrategy),
        ("min", MinStrategy),
        ("MIN", MinStrategy),
        ("mIn", MinStrategy),
    ],
)
def test_strategies_fabric(mock_coalescing_strategy, expected_instanced_strategy):
    """
    GIVEN a Type of strategy as a string value
    WHEN getting the corresponding instanced strategy
    THEN an object of a correct strategy is returned
    """
    assert isinstance(
        CoalescingStrategyFabric.get_strategy(mock_coalescing_strategy),
        expected_instanced_strategy,
    )
