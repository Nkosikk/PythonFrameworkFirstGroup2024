from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutCompletePage:
    checkoutComplete_xpath = "//span[contains(@data-test,'title')]"
    confirmationMessage_id = "//h2[@class='complete-header'][contains(.,'Thank you for your order!')]"
    # backHome_xpath = "//button[contains(@data-test,'back-to-products')]"
    burgerMenuButton_xpath = "//button[contains(.,'Open Menu')]"
    logoutButton_xpath = "//a[contains(@id,'link')][@class='bm-item menu-item'][contains(.,'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    # def clickBackHomeButton(self):
    #     wait = WebDriverWait(self.driver, 30)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.backHome_xpath)))
    #     element.click()

    def clickBurgerMenuButton(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.burgerMenuButton_xpath)))
        element.click()

    def clickLogoutButton(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.logoutButton_xpath)))
        element.click()
