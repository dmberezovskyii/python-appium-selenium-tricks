import logging
import pathlib
import os
import time
from enum import Enum


class LogLevel(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def __init__(self, log_lvl=LogLevel.INFO):
        self._log = logging.getLogger("appium")
        self._log.setLevel(LogLevel.DEBUG.value)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        self.log_file = self._create_log_file()
        self._configure_logging(log_lvl, formatter)

    def _create_log_file(self):
        current_time = time.strftime("%Y-%m-%d")
        log_directory = "logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
        base_dir = pathlib.Path(__file__).parent
        return str(base_dir.joinpath(log_directory, f"log{current_time}.log"))

    def _configure_logging(self, log_lvl, formatter):
        fh = logging.FileHandler(self.log_file, mode="w")
        fh.setFormatter(formatter)
        fh.setLevel(log_lvl.value)
        self._log.addHandler(fh)

    def get_instance(self):
        return self._log


if __name__ == "__main__":
    log = Logger(log_lvl=LogLevel.DEBUG).get_instance()
    log1 = Logger(log_lvl=LogLevel.DEBUG).get_instance()
    assert log is log1

    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log1.error("error")
    log1.info("info")
    log1.warning("warning")
    log1.error("error")
