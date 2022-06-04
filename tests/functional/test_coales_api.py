def test_coaslesce_api_with_valid_member_id_and_default_strategy(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/coalesce-api' page is requested (GET) with a valid member and without passing the strategy
    THEN check that the response is valid for that user and the values corresponding to a mean strategy
    """
    response = test_client.get("/coalesce-api?member_id=1")
    assert response.status_code == 200
    assert b'{"deductible":1066,"oop_max":5666,"stop_loss":11000}' in response.data


def test_coaslesce_api_with_valid_member_id_and_explicit_strategy(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/coalesce-api' page is requested (GET) with a valid member
    THEN check that the response is valid
    """
    response = test_client.get("/coalesce-api?member_id=1&coalescing_strategy=mean")
    assert response.status_code == 200
    assert b'{"deductible":1066,"oop_max":5666,"stop_loss":11000}' in response.data


def test_coaslesce_api_with_invalid_member_id(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/coalesce-api' page is requested (GET) with a valid member
    THEN check that the response is valid
    """
    invalid_member_id = 6
    response = test_client.get(
        f"/coalesce-api?member_id={invalid_member_id}&coalescing_strategy=mean"
    )
    assert response.status_code == 404
