import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from utils.readProperties import ReadConfig


class Test_001_LoginToSauceDemo:
    BaseUrl = ReadConfig().getBaseURL()
    Username = ReadConfig().getUsername()
    Password = ReadConfig().getPassword()

    @pytest.mark.nkosi
    @pytest.mark.loginSuccess
    @allure.severity(allure.severity_level.CRITICAL)
    def test_VerifyloginSuccessTests(self, setup):
        self.driver = setup
        self.driver.get(self.BaseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.lp.enterUsername(self.Username)
        self.lp.enterPassword(self.Password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Page", attachment_type=AttachmentType.PNG)
        self.lp.clickLoginButton()

        productText = self.driver.find_element(By.XPATH,self.hp.label_product_xpath).text

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
    def test_VerifyErrorMessageIsReturnedWhenYouLoginWithInvalidDetailsTests(self, setup):
        self.driver = setup
        self.driver.get(self.BaseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.lp.enterUsername(self.Username+"Nkosi")
        self.lp.enterPassword(self.Password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Page", attachment_type=AttachmentType.PNG)
        self.lp.clickLoginButton()

        loginError = self.driver.find_element(By.XPATH,self.lp.label_loginError_xpath).text

        if loginError == "Epic sadface: Username and password do not match any user in this service":
            allure.attach(self.driver.get_screenshot_as_png(), name="Invalid Login", attachment_type=AttachmentType.PNG)
            print("Invalid login validation passed")
            assert True
        else:
            print("Invalid login validation failed")
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Error validation failed", attachment_type=AttachmentType.PNG)
            assert False

        self.driver.quit()

