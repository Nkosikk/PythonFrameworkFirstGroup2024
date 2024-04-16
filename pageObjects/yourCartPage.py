from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait


class YourCartPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("BaseUrl")
        self.shoppingCart_xpath = "//a[contains(@class,'shopping_cart_link')]"
        self.yourCartLabel_xpath = "//span[@class='title'][contains(.,'Your Cart')]"
        self.sauceLabsBackpack_xpath = "//div[@class='inventory_item_name'][contains(.,'Sauce Labs Backpack')]"
        self.checkout_xpath = "//button[@id='checkout']"

    def clickNavigateToCart(self):
        element = wait.until(EC.element_to_be_clickable((By.ID, self.shoppingCart_xpath)))
        element.click()

    def verifyYourCartLabelIsDisplayedInCartPage(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.yourCartLabel_xpath)))
        yourCartText = self.driver.find_element(By.XPATH, self.yourCartLabel_xpath).text
        assert yourCartText == "Your Cart"

    def verifySauceLabsBackpackProductIsDisplayedInCartPage(self):
        ProductTextInCartPage = self.driver.find_element(By.XPATH, self.sauceLabsBackpack_xpath).text
        assert ProductTextInCartPage == "Sauce Labs Backpack"

    def clickCheckout(self):
        element = wait.until(EC.element_to_be_clickable((By.ID, self.checkout_xpath)))
        element.click()