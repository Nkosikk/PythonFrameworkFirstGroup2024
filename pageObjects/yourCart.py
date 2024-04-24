from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YourCartPage:
    yourCart_xpath = "//span[@class='title'][contains(.,'Your Cart')]"
    sauceLabsBack_xpath = "//div[contains(@class,'cart_item_label')]"
    checkout_xpath = "//button[contains(.,'Checkout')]"
    continueShopping_xpath = "//button[contains( @ id, 'continue-shopping')]"
    removeItem_xpath = "//button[contains(@id,'remove-sauce-labs-backpack')]"

    def __init__(self, driver):
        self.driver = driver

    def clickRemoveButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.removeItem_xpath)))
        element.click()

    def clickContinueShoppingButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.continueShopping_xpath)))
        element.click()

    def clickCheckoutButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.checkout_xpath)))
        element.click()
