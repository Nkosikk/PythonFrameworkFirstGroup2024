from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YourCartPage:
    yourCart_xpath = "//span[@class='title'][contains(.,'Your Cart')]"
    sauceLabsBack_xpath = "//div[contains(@class,'cart_item_label')]"
    checkout_xpath = "//button[contains(.,'Checkout')]"

    def __init__(self, driver):
        self.driver = driver

    def clickCheckOutButton(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.checkout_xpath)))
        element.click()
