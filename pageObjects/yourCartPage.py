from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YourCartPage:
    label_YourCart_xpath = "//span[@class='title'][contains(.,'Your Cart')]"
    label_SauceLabsBack_xpath = "//div[@class='inventory_item_name'][contains(.,'Sauce Labs Backpack')]"
    button_checkout_id = "checkout"


    def __init__(self, driver):
        self.driver = driver


    def clickCheckOutButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.button_checkout_id)))
        element.click()

