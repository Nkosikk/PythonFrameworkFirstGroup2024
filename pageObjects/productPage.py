from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.addToCartButton_id = "add-to-cart-sauce-labs-backpack"

    def clickAddToCartButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.addToCartButton_id)))
        element.click()