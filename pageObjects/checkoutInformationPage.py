from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutInformationPage:
    checkoutYourInformation_xpath = "//span[@class='title'][contains(.,'Checkout: Your Information')]"
    firstNameField_id = "first-name"
    lastNameField_id = "last-name"
    postalCodeField_id = "postal-code"
    continueButton_id = "continue"

    def __init__(self, driver):
        self.driver = driver

    def verifyCheckoutYourInformationPage(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.checkoutYourInformation_xpath)))
        checkoutText = self.driver.find_element(By.XPATH, self.checkoutYourInformation_xpath).text
        assert checkoutText == "Checkout: Your Information"

    def enterFirstName(self, fullname):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.firstNameField_id)))
        element.send_keys("Zamantuli")

    def enterLastName(self, surname):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.lastNameField_id)))
        element.send_keys("Ntuli")

    def enterPostalCode(self, zipcode):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.postalCodeField_id)))
        element.send_keys("1939")

    def clickContinueButton(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.continueButton_id)))
        element.click()
