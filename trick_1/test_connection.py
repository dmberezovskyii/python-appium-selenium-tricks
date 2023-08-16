# test_connections.py
from unittest.mock import Mock
import pytest
from trick_1 import Connections
import os

@pytest.fixture
def mock_driver():
    return Mock()

def test_check_connection_connected(mock_driver):
    mock_resp = {
        'networks': [{'isConnected': True}]
    }
    mock_driver.execute_script.return_value = mock_resp

    connections = Connections(mock_driver)
    result = connections.check_connection()

    assert result == True

def test_check_connection_not_connected(mock_driver):
    mock_resp = {
        'networks': [{'isConnected': False}]
    }
    mock_driver.execute_script.return_value = mock_resp

    connections = Connections(mock_driver)
    result = connections.check_connection()

    assert result == False

def test_use_secret():
    secret_value = os.environ["API_KEY"]
    assert secret_value is not None, "Secret not available"


# Add more test cases as needed
