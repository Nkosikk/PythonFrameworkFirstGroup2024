from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    label_product_xpath = "//span[@class='title'][contains(.,'Products')]"
    button_addToCartSauceBackLab_id = "add-to-cart-sauce-labs-backpack"
    button_AddedToCart_xpath = "//span[@class='shopping_cart_badge'][contains(.,'1')]"

    def __init__(self, driver):
        self.driver = driver

    def clickAddToCartSauceBackLabButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.button_addToCartSauceBackLab_id)))
        element.click()

    def clickShoppingCartButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_AddedToCart_xpath)))
        element.click()
