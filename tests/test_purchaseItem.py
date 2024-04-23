import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from pageObjects.CheckoutComplete import CheckoutCompletePage
from pageObjects.checkoutInformation import CheckoutInformationPage
from pageObjects.checkoutOverview import CheckoutOverviewPage
from pageObjects.home import HomePage
from pageObjects.login import LoginPage
from pageObjects.yourCart import YourCartPage
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
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.yourCartPage = YourCartPage(self.driver)
        self.checkoutInformationPage = CheckoutInformationPage(self.driver)
        self.checkoutOverviewPage = CheckoutOverviewPage(self.driver)
        self.checkoutCompletePage = CheckoutCompletePage(self.driver)
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

        self.homePage.clickAddToCartButton()
        self.driver.find_element(By.XPATH, self.homePage.AddedToCart_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Item Added to cart",
                      attachment_type=AttachmentType.PNG)

        self.homePage.clickShoppingCartButton()
        self.driver.find_element(By.XPATH, self.yourCartPage.yourCart_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Your Cart", attachment_type=AttachmentType.PNG)

        self.yourCartPage.clickRemoveButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Your Cart after removing the item", attachment_type=AttachmentType.PNG)

        self.yourCartPage.clickContinueShoppingButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Swag Labs", attachment_type=AttachmentType.PNG)

        self.homePage.clickAddToCartButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home Page", attachment_type=AttachmentType.PNG)

        self.homePage.clickShoppingCartButton()
        self.driver.find_element(By.XPATH, self.yourCartPage.yourCart_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Your Cart", attachment_type=AttachmentType.PNG)

        self.driver.find_element(By.XPATH, self.yourCartPage.sauceLabsBack_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Your Cart confirming the item details", attachment_type=AttachmentType.PNG)

        self.yourCartPage.clickCheckoutButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Your Information", attachment_type=AttachmentType.PNG)

        self.driver.find_element(By.XPATH, self.checkoutInformationPage.checkoutYourInformation_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Your Information", attachment_type=AttachmentType.PNG)

        self.checkoutInformationPage.enterFirstName(self.FullName)
        self.checkoutInformationPage.enterLastName(self.Surname)
        self.checkoutInformationPage.enterPostalCode(self.ZipCode)
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Your Information - details inserted", attachment_type=AttachmentType.PNG)

        self.checkoutInformationPage.clickCancelButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Your Cart", attachment_type=AttachmentType.PNG)

        self.yourCartPage.clickCheckoutButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Your Information", attachment_type=AttachmentType.PNG)

        self.checkoutInformationPage.enterFirstName(self.FullName)
        self.checkoutInformationPage.enterLastName(self.Surname)
        self.checkoutInformationPage.enterPostalCode(self.ZipCode)
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Your Information - details inserted", attachment_type=AttachmentType.PNG)

        self.checkoutInformationPage.clickContinueButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Overview", attachment_type=AttachmentType.PNG)
        self.driver.find_element(By.XPATH, self.checkoutOverviewPage.checkoutOverview_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.checkoutOverviewPage.sauceLabsBackpack_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Your Information confirming the item details", attachment_type=AttachmentType.PNG)

        self.checkoutOverviewPage.verifyItemTotalPlusTaxEqualsTotal()

        self.checkoutOverviewPage.clickCancelButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home Page", attachment_type=AttachmentType.PNG)

        self.homePage.clickShoppingCartButton()
        self.driver.find_element(By.XPATH, self.yourCartPage.yourCart_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Your Cart", attachment_type=AttachmentType.PNG)

        self.driver.find_element(By.XPATH, self.yourCartPage.sauceLabsBack_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Your Cart confirming the item details", attachment_type=AttachmentType.PNG)

        self.yourCartPage.clickCheckoutButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Your Information", attachment_type=AttachmentType.PNG)

        self.driver.find_element(By.XPATH, self.checkoutInformationPage.checkoutYourInformation_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Your Information", attachment_type=AttachmentType.PNG)

        self.checkoutInformationPage.enterFirstName(self.FullName)
        self.checkoutInformationPage.enterLastName(self.Surname)
        self.checkoutInformationPage.enterPostalCode(self.ZipCode)
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Your Information - details inserted", attachment_type=AttachmentType.PNG)

        self.checkoutInformationPage.clickContinueButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Overview", attachment_type=AttachmentType.PNG)
        self.driver.find_element(By.XPATH, self.checkoutOverviewPage.checkoutOverview_xpath).is_displayed()
        self.driver.find_element(By.XPATH, self.checkoutOverviewPage.sauceLabsBackpack_xpath).is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Your Information confirming the item details", attachment_type=AttachmentType.PNG)

        self.checkoutOverviewPage.verifyItemTotalPlusTaxEqualsTotal()

        self.checkoutOverviewPage.clickFinishButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Complete!", attachment_type=AttachmentType.PNG)

        self.driver.find_element(By.XPATH, self.checkoutCompletePage.checkoutComplete_xpath)
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout: Complete! screen", attachment_type=AttachmentType.PNG)

        self.driver.find_element(By.XPATH, self.checkoutCompletePage.confirmationMessage_id)
        allure.attach(self.driver.get_screenshot_as_png(), name="Thank you for your order!", attachment_type=AttachmentType.PNG)

        # self.checkoutCompletePage.clickBackHomeButton()
        # allure.attach(self.driver.get_screenshot_as_png(), name="Home Page", attachment_type=AttachmentType.PNG)

        self.checkoutCompletePage.clickBurgerMenuButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout Complete - Swag Labs", attachment_type=AttachmentType.PNG)

        self.checkoutCompletePage.clickLogoutButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Screen - Swag Labs", attachment_type=AttachmentType.PNG)

        self.driver.quit()
