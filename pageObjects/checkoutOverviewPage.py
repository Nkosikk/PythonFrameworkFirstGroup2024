from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:

    checkoutOverview_xpath = "//span[@class='title'][contains(.,'Checkout: Overview')]"
    sauceLabsBackpack_xpath = "//div[@class='inventory_item_name'][contains(.,'Sauce Labs Backpack')]"
    itemPrice_xpath = "//div[@class='summary_subtotal_label']"
    total_xpath = "//div[@class='summary_info_label summary_total_label']"
    finishButton_id = "finish"
    cancelButton_id = "cancel"
    burgerMenuButton_id = "//button[contains(@id,'react-burger-menu-btn')]"
    logoutButton_id = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def calculate_total(self, total_xpath, tax):
        # Calculate the sum of item total and tax
        itemPrice_xpath = total_xpath + tax
        return itemPrice_xpath

    def clickFinishButton(self):
        element = wait.until(EC.element_to_be_clickable((By.ID, self.finishButton_id)))
        element.click()

    def clickCancelButton(self):
        element = wait.until(EC.element_to_be_clickable((By.ID, self.cancelButton_id)))
        element.click()

    def clickBurgerMenuButton(self):
        element = wait.until(EC.element_to_be_clickable((By.ID, self.burgerMenuButton_id)))
        element.click()

    def clickLogoutFromBurgerMenu(self):
        element = wait.until(EC.element_to_be_clickable((By.ID, self.logoutButton_id)))
        element.click()
