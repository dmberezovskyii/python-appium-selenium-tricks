from BaseScreen import Base
from appium.webdriver.common.mobileby import MobileBy


class LoginScreen(Base):
    ADD_CITY = (MobileBy.ACCESSIBILITY_ID, 'Login btn')

    def __init__(self, driver):
        super().__init__(driver)

    def tap_login_btn(self):
        pass
