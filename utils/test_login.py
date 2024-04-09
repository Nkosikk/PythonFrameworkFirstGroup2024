import allure
import pytest

from pageObjects.loginPage import LoginPage
from utils.readProperties import ReadConfig


class test_001_LoginToSauceDemo:
    BaseUrl = ReadConfig().getBaseURL()
    Username = ReadConfig().getUsername()
    Password = ReadConfig().getPassword()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginTests(self, setup):
        self.driver = setup
        self.driver.get(self.BaseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.Username)
        self.lp.enterPassword(self.Password)
        self.lp.clickLoginButton()