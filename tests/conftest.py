import pytest

from src import create_app
from src.resources.coalesce.coalesce import Coalesce
from src.resources.coalesce.strategies.max_strategy import MaxStrategy
from src.resources.coalesce.strategies.mean_strategy import MeanStrategy
from src.resources.coalesce.strategies.median_strategy import MedianStrategy
from src.resources.coalesce.strategies.min_strategy import MinStrategy
from src.resources.coalesce.strategies.mode_strategy import ModeStrategy


@pytest.fixture()
def coalesce_mean():
    return Coalesce(strategy=MeanStrategy())


@pytest.fixture()
def coalesce_median():
    return Coalesce(strategy=MedianStrategy())


@pytest.fixture()
def coalesce_mode():
    return Coalesce(strategy=ModeStrategy())


@pytest.fixture()
def coalesce_max():
    return Coalesce(strategy=MaxStrategy())


@pytest.fixture()
def coalesce_min():
    return Coalesce(strategy=MinStrategy())


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app("flask_test.cfg")

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client
