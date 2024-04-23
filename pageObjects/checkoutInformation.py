from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutInformationPage:
    checkoutYourInformation_xpath = "//span[@class='title'][contains(.,'Checkout: Your Information')]"
    firstNameField_xpath = "//input[contains(@id,'first-name')]"
    lastNameField_xpath = "//input[contains(@id,'last-name')]"
    postalCodeField_xpath = "//input[contains(@id,'postal-code')]"
    cancelButton_xpath = "//button[@data-test='cancel']"
    continueButton_xpath = "//input[contains(@type,'submit')]"

    def __init__(self, driver):
        self.driver = driver

    def enterFirstName(self, firstname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.firstNameField_xpath)))
        element.send_keys(firstname)

    def enterLastName(self, lastname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.lastNameField_xpath)))
        element.send_keys(lastname)

    def enterPostalCode(self, zipcode):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.postalCodeField_xpath)))
        element.send_keys(zipcode)

    def clickCancelButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.cancelButton_xpath)))
        element.click()

    def clickContinueButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.continueButton_xpath)))
        element.click()
