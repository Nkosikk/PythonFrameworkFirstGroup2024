import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from pageObjects.checkoutInformationPage import CheckoutInformationPage
from pageObjects.checkoutOverviewPage import CheckoutOverviewPage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.yourCartPage import YourCartPage
from utils.readProperties import ReadConfig


class Test_003_LoginToSauceDemo:
    BaseUrl = ReadConfig().getBaseURL()
    Username = ReadConfig().getUsername()
    Password = ReadConfig().getPassword()
    FullName = ReadConfig().getFullName()
    Surname = ReadConfig().getSurname()
    ZipCode = ReadConfig().getZipCode()

    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_purchaseItemTests(self, setup):
        self.driver = setup
        self.driver.get(self.BaseUrl)  # This line is passing the url of the system in test
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.ycp = YourCartPage(self.driver)
        self.cip = CheckoutInformationPage(self.driver)
        self.cop = CheckoutOverviewPage(self.driver)
        self.lp.enterUsername(self.Username)
        self.lp.enterPassword(self.Password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Page", attachment_type=AttachmentType.PNG)
        self.lp.clickLoginButton()

        productText = self.driver.find_element(By.XPATH, self.hp.product_xpath).text

        if productText == "Products":
            print("Login Success")
            allure.attach(self.driver.get_screenshot_as_png(), name="Home Page", attachment_type=AttachmentType.PNG)
            assert True
        else:
            print("Login Failed")
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Failed", attachment_type=AttachmentType.PNG)
            assert False
        self.hp.clickAddToCartButton()
        self.driver.find_element(By.XPATH, self.hp.AddedToCart_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Item Added to cart",
                      attachment_type=AttachmentType.PNG)

        self.hp.clickShoppingCartButton()

        self.driver.find_element(By.XPATH, self.ycp.yourCart_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Your Cart", attachment_type=AttachmentType.PNG)

        self.driver.find_element(By.XPATH, self.ycp.sauceLabsBack_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Sauce Labs Backpack",
                      attachment_type=AttachmentType.PNG)

        self.ycp.clickCheckOutButton()
        self.driver.find_element(By.XPATH, self.cip.checkoutYourInformation_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Your Information", attachment_type=AttachmentType.PNG)
        self.cip.enterFirstName(self.FullName)
        self.cip.enterLastName(self.Surname)
        self.cip.enterPostalCode(self.ZipCode)

        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Your Information", attachment_type=AttachmentType.PNG)

        self.cip.clickContinueButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Overview", attachment_type=AttachmentType.PNG)

        self.cop.verifyItemTotalPlusTaxEqualsTotal()

        # self.cop.clickFinishButton()
        # allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Complete!",
        #               attachment_type=AttachmentType.PNG)
        #
        # self.cop.clickCancelButton()
        # allure.attach(self.driver.get_screenshot_as_png(), name="Home Page", attachment_type=AttachmentType.PNG)
        #
        # self.cop.clickBurgerMenuButton()
        #
        # self.cop.clickLogoutFromBurgerMenu()
        # allure.attach(self.driver.get_screenshot_as_png(), name="Swag Labs", attachment_type=AttachmentType.PNG)

        self.driver.quit()
