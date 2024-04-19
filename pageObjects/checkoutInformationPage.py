from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutInformationPage:
    checkoutYourInformation_xpath = "//span[@class='title'][contains(.,'Checkout: Your Information')]"
    firstNameField_xpath = "//input[contains(@id,'first-name')]"
    lastNameField_xpath = "//input[contains(@id,'last-name')]"
    postalCodeField_xpath = "//input[contains(@id,'postal-code')]"
    continueButton_xpath = "//input[contains(@id,'continue')]"

    def __init__(self, driver):
        self.driver = driver

    # def verifyCheckoutYourInformationPage(self):
    #     WebDriverWait(self.driver, 30).until(
    #         EC.visibility_of_element_located((By.XPATH, self.checkoutYourInformation_xpath)))
    #     checkoutText = self.driver.find_element(By.XPATH, self.checkoutYourInformation_xpath).text
    #     assert checkoutText == "Checkout: Your Information"

    def enterFirstName(self, firstname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.firstNameField_xpath)))
        element.send_keys("firstname")

    def enterLastName(self, lastname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.lastNameField_xpath)))
        element.send_keys("lastname")

    def enterPostalCode(self, postcode):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.postalCodeField_xpath)))
        element.send_keys("postcode")

    def clickContinueButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.continueButton_xpath)))
        element.click()
