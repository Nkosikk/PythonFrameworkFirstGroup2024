from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:
    checkoutOverview_xpath = "//span[@class='title'][contains(.,'Checkout: Overview')]"
    sauceLabsBackpack_xpath = "//div[@data-test='inventory-item-name']"
    itemPrice_xpath = "//div[@data-test='subtotal-label']"
    total_xpath = "//div[@data-test='total-label']"
    finishButton_xpath = "//button[contains(@id,'finish')]"
    cancelButton_xpath = "//button[contains(@id,'cancel')]"

    def __init__(self, driver):
        self.driver = driver

    def verifyItemTotalPlusTaxEqualsTotal(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.itemPrice_xpath))).text

        # Resolve Tax
        itemPriceText = element.replace("Item total: $", "")
        itemPrice = float(itemPriceText)
        print(itemPrice)

        # Calculate Item Total plus Tax
        FullItemPricePlusTax = itemPrice + (itemPrice * 0.08)
        ItemPricePlusTax = round(FullItemPricePlusTax, 2)
        print(ItemPricePlusTax)

        # Resolve Total
        element2 = wait.until(EC.element_to_be_clickable((By.XPATH, self.total_xpath))).text
        totalText = element2.replace("Total: $", "")
        Total = float(totalText)
        print(Total)

    def clickCancelButton(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.cancelButton_xpath)))
        element.click()

    def clickFinishButton(self):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.finishButton_xpath)))
        element.click()

    # def verify_confirmation_message(self):
    #     confirmation_message = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.ID, self.confirmationMessage_id))
    #     )
    #     return "Thank you for your order!" in confirmation_message.text

    # assert True
    # else:
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.cancelButton_xpath)))
    #     element.click()
    #     print("")
    #
    # def clickBurgerMenuButton(self):
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.burgerMenuButton_xpath)))
    #     element.click()
    #
    # def clickLogoutFromBurgerMenu(self):
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.logoutButton_xpath)))
    #     element.click()
    # assert False
