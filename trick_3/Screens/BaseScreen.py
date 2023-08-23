from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

Locator = Tuple[By, str]


class Base:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, 15)
        self._short_wait = WebDriverWait(driver, 5)
        self.log_wait = WebDriverWait(driver, 100)

    def wait(self, locator: Locator, waiter: WebDriverWait = None) -> WebElement:
        if waiter is None:
            waiter = self._wait
        return waiter.until(EC.presence_of_element_located(locator))

    def short_wait(self, locator: Locator) -> WebElement:
        return self.wait(locator, waiter=self._short_wait)
