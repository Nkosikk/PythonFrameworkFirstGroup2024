import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from utils.readProperties import ReadConfig


class Test_002_LoginToSauceDemo:
    BaseUrl = ReadConfig().getBaseURL()
    Username = ReadConfig().getUsername()
    Password = ReadConfig().getPassword()

    @pytest.mark.nkosi
    @pytest.mark.AddItem
    @allure.severity(allure.severity_level.CRITICAL)
    def test_1_AddItemToCartTests(self, setup):
        self.driver = setup
        self.driver.get(self.BaseUrl)  # This line is passing the url of the system in test
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
        self.hp.clickAddToCartSauceBackLabButton()
        self.driver.find_element(By.XPATH, self.hp.button_AddedToCart_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Item Added to cart", attachment_type=AttachmentType.PNG)



        self.driver.quit()
