import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from pageObjects.home import HomePage
from pageObjects.login import LoginPage
from utils.readProperties import ReadConfig


class Test_001_LoginToSauceDemo:
    BaseUrl = ReadConfig().getBaseURL()
    Username = ReadConfig().getUsername()
    Password = ReadConfig().getPassword()

    @pytest.mark.nkosi
    @pytest.mark.loginSuccess
    @allure.severity(allure.severity_level.CRITICAL)
    def test_1_VerifyLoginSuccessTests(self, setup):
        self.driver = setup
        self.driver.get(self.BaseUrl)  # This line is passing the url of the system in test
        self.driver.maximize_window()
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage.enterUsername(self.Username)
        self.loginPage.enterPassword(self.Password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Page", attachment_type=AttachmentType.PNG)
        self.loginPage.clickLoginButton()

        productText = self.driver.find_element(By.XPATH, self.homePage.product_xpath).text

        if productText == "Products":
            print("Login Success")
            allure.attach(self.driver.get_screenshot_as_png(), name="Home Page", attachment_type=AttachmentType.PNG)
            assert True
        else:
            print("Login Failed")
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Failed", attachment_type=AttachmentType.PNG)
            assert False

        self.driver.quit()

    @pytest.mark.nkosi
    @pytest.mark.loginUncessuss
    @allure.severity(allure.severity_level.CRITICAL)
    def test_2_VerifyErrorMessageIsReturnedWhenYouLoginWithInvalidDetailsTests(self, setup):
        self.driver = setup
        self.driver.get(self.BaseUrl)
        self.driver.maximize_window()
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage.enterUsername(self.Username+"Nkosi")
        self.loginPage.enterPassword(self.Password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Page", attachment_type=AttachmentType.PNG)
        self.loginPage.clickLoginButton()

        loginError = self.driver.find_element(By.XPATH, self.loginPage.loginError_xpath).text

        if loginError == "Epic sadface: Username and password do not match any user in this service":
            allure.attach(self.driver.get_screenshot_as_png(), name="Invalid Login", attachment_type=AttachmentType.PNG)
            print("Invalid login validation passed")
            assert True
        else:
            print("Invalid login validation failed")
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Error validation failed", attachment_type=AttachmentType.PNG)
            assert False

        self.driver.quit()

