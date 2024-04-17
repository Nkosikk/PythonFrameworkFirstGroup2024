from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutInformationPage:
    textbox_firstname_id = "first-name"
    textbox_lastname_id = "last-name"
    textbox_zipcode_id = "postal-code"
    button_continue_id = "continue"
    label_checkoutInformationPage_xpath = "//span[@class='title'][contains(.,'Checkout: Your Information')]"

    def __init__(self, driver):
        self.driver = driver

    def enterFirstName(self, Fullname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.textbox_firstname_id)))
        element.send_keys("first-name")

    def enterLastName(self, Surname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.textbox_lastname_id)))
        element.send_keys("last-name")

    def enterZipCode(self, Zipcode):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.textbox_zipcode_id)))
        element.send_keys("postal-code")

    def clickContinueButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.button_continue_id)))
        element.click()