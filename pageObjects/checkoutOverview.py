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
