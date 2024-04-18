from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutYourInformation:
    label_CheckoutYourInformation_xpath = "//span[@class='title'][contains(.,'Checkout: Your Information')]"
    textbox_FirstName_xpath = "//input[contains(@id,'first-name')]"
    textbox_LastName_xpath = "//input[contains(@placeholder,'Last Name')]"
    textbox_PostCode_xpath = "//input[contains(@placeholder,'Zip/Postal Code')]"
    button_Continue_xpath = "//input[contains(@type,'submit')]"


    def __init__(self, driver):
        self.driver = driver


    def enterFirstName(self, firstname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_FirstName_xpath)))
        element.send_keys(firstname)

    def enterLastName(self, lastname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_LastName_xpath)))
        element.send_keys(lastname)

    def enterPostCode(self, postcode):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.textbox_PostCode_xpath)))
        element.send_keys(postcode)

    def clickContinueButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_Continue_xpath)))
        element.click()