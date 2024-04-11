import allure
import pytest
from allure_commons.types import AttachmentType

from pageObjects.loginPage import LoginPage
from utils.readProperties import ReadConfig


class Test_001_LoginToSauceDemo:

    BaseUrl = ReadConfig().getBaseURL()
    Username = ReadConfig().getUsername()
    Password = ReadConfig().getPassword()

    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.BLOCKER)
    def test_loginTests(self,setup):
        self.driver = setup
        self.driver.get(self.BaseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.Username)
        self.lp.enterPassword(self.Password)
        allure.attach(self.driver.get_screenshot_as_png(),name="Login Page",attachment_type=AttachmentType.PNG)
        self.lp.clickLoginButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home Page", attachment_type=AttachmentType.PNG)




        self.driver.quit()
