from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YourCartPage:
    label_YourCart_xpath = "//span[@class='title'][contains(.,'Your Cart')]"
    button_Checkout_xpath = "//button[contains(.,'Checkout')]"
   # button_AddedToCart_xpath = "//span[@class='shopping_cart_badge'][contains(.,'1')]"




    def __init__(self, driver):
        self.driver = driver

    def clickAddToCartSauceBackLabButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_addToCartSauceBackLab_id)))
        element.click()

    def clickChackoutButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_Checkout_xpath)))
        element.click()




