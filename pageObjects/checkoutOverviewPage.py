from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:
    checkoutOverview_xpath = "//span[@class='title'][contains(.,'Checkout: Overview')]"
    sauceLabsBackpack_xpath = "//div[@class='inventory_item_name'][contains(.,'Sauce Labs Backpack')]"
    itemPrice_xpath = "//div[@class='summary_subtotal_label']"
    total_xpath = "//div[@class='summary_info_label summary_total_label']"
    finishButton_xpath = "//button[contains(@id,'finish')]"
    cancelButton_xpath = "//button[contains(@id,'cancel')]"
    burgerMenuButton_xpath = "//button[contains(@id,'react-burger-menu-btn')]"
    logoutButton_xpath = "//a[contains(@id,'link')][@class='bm-item menu-item'][contains(.,'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    def verifyItemTotalPlusTaxEqualsTotal(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.itemPrice_xpath))).text

        # Resolve Tax
        itemPriceText = element.replace("Item total: $","")
        itemPrice = float(itemPriceText)
        print(itemPrice)

        # Calculate Item Total plus Tax
        FullItemPricePlusTax = itemPrice+(itemPrice*0.08)
        ItemPricePlusTax = round(FullItemPricePlusTax,2)
        print(ItemPricePlusTax)

        # Resolve Total
        element2 = wait.until(EC.element_to_be_clickable((By.XPATH, self.total_xpath))).text
        totalText = element2.replace("Total: $", "")
        Total = float(totalText)
        print(Total)

    # if ItemTotalPlusTax == Total:
    # def clickFinishButton(self):
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.finishButton_xpath)))
    #     element.click()
    #
    # assert True
    # def clickCancelButton(self):
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.cancelButton_xpath)))
    #     element.click()
    #
    # def clickBurgerMenuButton(self):
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.burgerMenuButton_xpath)))
    #     element.click()
    #
    # def clickLogoutFromBurgerMenu(self):
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.logoutButton_xpath)))
    #     element.click()
    # assert False
