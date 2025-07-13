import pytest
# Import the Flask app instance from your main application file.
# Assuming your Flask app file is named 'flaskApp.py'
from flaskApp import app

# This is a pytest fixture. A fixture is a function that runs before
# each test function (or once per session/module, depending on scope)
# to provide a setup for the tests.
# Here, it creates a test client for the Flask application.
# The 'yield' keyword makes it a teardown fixture, meaning the code
# after 'yield' runs after the test has completed.
@pytest.fixture
def client():
    # Configure the app for testing.
    # This disables error catching during tests, allowing exceptions to propagate.
    app.config['TESTING'] = True
    # Create a test client using Flask's built-in test_client().
    with app.test_client() as client:
        yield client # This client is passed to the test functions

# Test for the home page route ("/")
def test_home_page(client):
    # Make a GET request to the home URL
    response = client.get('/')
    # Assert that the HTTP status code is 200 (OK)
    assert response.status_code == 200
    # Assert that a specific string is present in the response data (HTML content)
    # The 'b' prefix means it's a byte string, as response.data is bytes.
    assert b"Welcome to the F1 Fan Zone!" in response.data
    assert b"Home" in response.data # Check for navigation link

# Test for the Max Verstappen page route ("/max-verstappen")
def test_max_verstappen_page(client):
    response = client.get('/max-verstappen')
    assert response.status_code == 200
    assert b"Max Verstappen: The Flying Dutchman" in response.data
    assert b"multiple Formula 1 World Champion" in response.data

# Test for the Red Bull Racing page route ("/red-bull-racing")
def test_red_bull_racing_page(client):
    response = client.get('/red-bull-racing')
    assert response.status_code == 200
    assert b"Red Bull Racing: The Energy Drink Giant in F1" in response.data
    assert b"founded in 2005" in response.data

# Test for the Formula 1 page route ("/formula-1")
def test_formula_1_page(client):
    response = client.get('/formula-1')
    assert response.status_code == 200
    assert b"Formula 1: The Pinnacle of Motorsport" in response.data
    assert b"highest class of international racing" in response.data

# Test for the Championships page route ("/championships")
def test_championships_page(client):
    response = client.get('/championships')
    assert response.status_code == 200
    assert b"Max Verstappen's Formula 1 World Championships" in response.data
    assert b"2021 Formula 1 World Champion" in response.data
    assert b"2022 Formula 1 World Champion" in response.data
    assert b"2023 Formula 1 World Champion" in response.data
