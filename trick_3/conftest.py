import pytest
from appium import webdriver


def pytest_addoption(parser) -> None:
    parser.addoption("--platform", action="store", default="android", help="Android OS used by default")


@pytest.fixture(scope="class", name="mobile_driver")
def fixture_mobile_driver(request):
    desired_caps = {'platformName': 'Android', 'deviceName': 'Android', 'appPackage': 'com.goibibo',
                    'appActivity': '.common.HomeActivity', 'noReset': True, 'isHeadless': True}
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
