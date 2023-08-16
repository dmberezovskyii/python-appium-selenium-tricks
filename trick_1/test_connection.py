# test_connections.py
from unittest.mock import Mock
import json
import pytest
from trick_1 import Connections

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

# Add more test cases as needed
