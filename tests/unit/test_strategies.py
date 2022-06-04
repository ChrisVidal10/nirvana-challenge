import pytest

from src.resources.coalesce.strategies.strategies_utils import StrategiesUtils


@pytest.mark.parametrize(
    "mock_dataset, expected_grouped_map",
    [
        (
            [
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000},
                {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000},
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000},
            ],
            {
                "deductible": [1000, 1200, 1000],
                "stop_loss": [10000, 13000, 10000],
                "oop_max": [5000, 6000, 6000],
            },
        ),
        (
            [
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000, "test": 100},
                {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000, "test": 200},
                {
                    "deductible": 1000,
                    "stop_loss": 10000,
                    "oop_max": 6000,
                    "another_test": 300,
                },
            ],
            {
                "deductible": [1000, 1200, 1000],
                "stop_loss": [10000, 13000, 10000],
                "oop_max": [5000, 6000, 6000],
                "test": [100, 200],
                "another_test": [300],
            },
        ),
        (
            [],
            {},
        ),
    ],
)
def test_grouped_list_of_satasets_by_keys(mock_dataset, expected_grouped_map):
    """
    GIVEN List of dictionaries
    WHEN grouping is requested
    THEN a dictionary with the union of all their values by key in a list is returned
    """
    assert expected_grouped_map == StrategiesUtils.group_by_key(mock_dataset)


@pytest.mark.parametrize(
    "mock_dataset, expected_result",
    [
        (
            [
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000},
                {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000},
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000},
            ],
            {
                "deductible": 1066,
                "stop_loss": 11000,
                "oop_max": 5666,
            },
        ),
        (
            [
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000, "test": 100},
                {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000, "test": 200},
                {
                    "deductible": 1000,
                    "stop_loss": 10000,
                    "oop_max": 6000,
                    "another_test": 300,
                },
            ],
            {
                "deductible": 1066,
                "stop_loss": 11000,
                "oop_max": 5666,
                "test": 150,
                "another_test": 300,
            },
        ),
        (
            [],
            {},
        ),
    ],
)
def test_mean_strategy(mock_dataset, expected_result, coalesce_mean):
    """
    GIVEN List of dictionaries
    WHEN each value is a dictionary with a pair key, integer value
    THEN a dictionary with arithmetic mean in its keys is returned
    """
    assert expected_result == coalesce_mean.execute_coalesce_strategy(mock_dataset)


@pytest.mark.parametrize(
    "mock_dataset, expected_result",
    [
        (
            [
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000},
                {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000},
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000},
            ],
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 6000,
            },
        ),
        (
            [
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000, "test": 100},
                {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000, "test": 200},
                {
                    "deductible": 1000,
                    "stop_loss": 10000,
                    "oop_max": 6000,
                    "another_test": 300,
                },
            ],
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 6000,
                "test": 150,
                "another_test": 300,
            },
        ),
        (
            [],
            {},
        ),
    ],
)
def test_median_strategy(mock_dataset, expected_result, coalesce_median):
    """
    GIVEN List of dictionaries
    WHEN each value is a dictionary with a pair key, integer value
    THEN a dictionary with the median in its keys is returned
    """
    assert expected_result == coalesce_median.execute_coalesce_strategy(mock_dataset)


@pytest.mark.parametrize(
    "mock_dataset, expected_result",
    [
        (
            [
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000},
                {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000},
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000},
            ],
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 6000,
            },
        ),
        (
            [
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000, "test": 100},
                {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000, "test": 200},
                {
                    "deductible": 1000,
                    "stop_loss": 10000,
                    "oop_max": 6000,
                    "another_test": 300,
                },
            ],
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 6000,
                "test": 100,
                "another_test": 300,
            },
        ),
        (
            [],
            {},
        ),
    ],
)
def test_mode_strategy(mock_dataset, expected_result, coalesce_mode):
    """
    GIVEN List of dictionaries
    WHEN each value is a dictionary with a pair key, integer value
    THEN a dictionary with the mode in its keys is returned
    """
    assert expected_result == coalesce_mode.execute_coalesce_strategy(mock_dataset)


@pytest.mark.parametrize(
    "mock_dataset, expected_result",
    [
        (
            [
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000},
                {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000},
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000},
            ],
            {
                "deductible": 1200,
                "stop_loss": 13000,
                "oop_max": 6000,
            },
        ),
        (
            [
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000, "test": 100},
                {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000, "test": 200},
                {
                    "deductible": 1000,
                    "stop_loss": 10000,
                    "oop_max": 6000,
                    "another_test": 300,
                },
            ],
            {
                "deductible": 1200,
                "stop_loss": 13000,
                "oop_max": 6000,
                "test": 200,
                "another_test": 300,
            },
        ),
        (
            [],
            {},
        ),
    ],
)
def test_max_strategy(mock_dataset, expected_result, coalesce_max):
    """
    GIVEN List of dictionaries
    WHEN each value is a dictionary with a pair key, integer value
    THEN a dictionary with the maximum value in its keys is returned
    """
    assert expected_result == coalesce_max.execute_coalesce_strategy(mock_dataset)


@pytest.mark.parametrize(
    "mock_dataset, expected_result",
    [
        (
            [
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000},
                {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000},
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000},
            ],
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 5000,
            },
        ),
        (
            [
                {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000, "test": 100},
                {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000, "test": 200},
                {
                    "deductible": 1000,
                    "stop_loss": 10000,
                    "oop_max": 6000,
                    "another_test": 300,
                },
            ],
            {
                "deductible": 1000,
                "stop_loss": 10000,
                "oop_max": 5000,
                "test": 100,
                "another_test": 300,
            },
        ),
        (
            [],
            {},
        ),
    ],
)
def test_min_strategy(mock_dataset, expected_result, coalesce_min):
    """
    GIVEN List of dictionaries
    WHEN each value is a dictionary with a pair key, integer value
    THEN a dictionary with the minimum value in its keys is returned
    """
    assert expected_result == coalesce_min.execute_coalesce_strategy(mock_dataset)
