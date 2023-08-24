import pathlib

import pytest
import logging
import time
from trick_5.Logger import Logger, LogLevel


def test_singleton_instance_creation():
    log_instance1 = Logger(log_lvl=LogLevel.DEBUG).get_instance()
    log_instance2 = Logger(log_lvl=LogLevel.DEBUG).get_instance()

    assert log_instance1 is log_instance2


def test_logger_functionality(tmp_path):
    log_instance = Logger(log_lvl=LogLevel.DEBUG)
    log_dir = pathlib.Path(__file__).parent / "logs"
    current_time = time.strftime("%Y-%m-%d")
    log_file_name = f"log{current_time}.log"
    log_file_path = log_dir / log_file_name

    log_instance.log_file = str(log_file_path)

    log = log_instance.get_instance()

    log.debug("debug message")
    log.info("info message")
    log.warning("warning message")
    log.error("error message")

    with open(log_file_path, "r") as log_file:
        content = log_file.read()
        assert "debug message" in content
        assert "info message" in content
        assert "warning message" in content
        assert "error message" in content


if __name__ == "__main__":
    pytest.main(["-s", __file__])
