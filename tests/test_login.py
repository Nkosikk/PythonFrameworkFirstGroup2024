import allure
import pytest
from allure_commons.types import AttachmentType
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from pageObjects.productPage import ProductPage
from pageObjects.yourCartPage import YourCartPage
from utils.readProperties import ReadConfig


class Test_001_LoginToSauceDemo:
    BaseUrl = ReadConfig().getBaseURL()
    Username = ReadConfig().getUsername()
    Password = ReadConfig().getPassword()
    FullName = ReadConfig().getFullNameL()
    Surname = ReadConfig().getSurname()
    ZipCode = ReadConfig().getZipCode()

    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.BLOCKER)
    def test_loginTests(self, setup):
        self.driver = setup
        self.driver.get(self.BaseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.Username)
        self.lp.enterPassword(self.Password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Page", attachment_type=AttachmentType.PNG)
        self.lp.clickLoginButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home Page", attachment_type=AttachmentType.PNG)

    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.BLOCKER)
    def test_HomeTests(self, setup):
         self.driver = setup
         self.hp = HomePage(self.driver)
         self.hp.verifyProductLabelIsDisplayedInHomePage()
         allure.attach(self.driver.get_screenshot_as_png(), name="Home Page", attachment_type=AttachmentType.PNG)

    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ProductsTests(self, setup):
        self.driver = setup
        self.pp = ProductPage(self.driver)
        self.pp.clickAddToCartButton()
        self.pp.clickNavigateToCart()
        allure.attach(self.driver.get_screenshot_as_png(), name="Products", attachment_type=AttachmentType.PNG)

    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.BLOCKER)
    def test_verifyYourCartLabelIsDisplayedInCartPageTests(self, setup):
        self.driver = setup
        self.ycp = YourCartPage(self.driver)
        self.ycp.clickNavigateToCart()
        self.ycp.verifyYourCartLabelIsDisplayedInCartPage()
        self.ycp.verifySauceLabsBackpackProductIsDisplayedInCartPage()
        allure.attach(self.driver.get_screenshot_as_png(), name="Your Cart Page",attachment_type=AttachmentType.PNG)
        self.ycp.clickCheckout()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Your Information",attachment_type=AttachmentType.PNG)

        #self.driver.quit()
