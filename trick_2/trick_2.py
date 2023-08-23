from typing import Tuple

from appium.webdriver import WebElement
from selenium.common import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

Locator = Tuple[By, str]


class BaseScreen:
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, 15)
        self._short_wait = WebDriverWait(driver, 5)
        self._long_wait = WebDriverWait(driver, 45)
        self._fl_wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[ElementNotVisibleException],
        )

    def wait(self, locator: Locator, waiter: WebDriverWait = None) -> WebElement:
        if waiter is None:
            waiter = self._wait
        return waiter.until(ec.presence_of_element_located(locator))

    def short_wait(self, locator: Locator) -> WebElement:
        return self.wait(locator, waiter=self._short_wait)

    def long_wait(self, locator: Locator) -> WebElement:
        return self.wait(locator, waiter=self._long_wait)

    def wait_until_visible(
        self, locator: Locator, waiter: WebDriverWait = None
    ) -> WebElement:
        if waiter is None:
            waiter = self._wait
        return waiter.until(ec.visibility_of_element_located(locator))
