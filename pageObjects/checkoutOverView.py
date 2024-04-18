from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverview:
    label_itemTotal_xpath = "//div[@data-test='subtotal-label']"
    label_Total_xpath = "//div[@data-test='total-label']"


    def __init__(self, driver):
        self.driver = driver


    def verifyItemTotalPlusTaxEqualsTotal(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.label_itemTotal_xpath))).text

        # Resolve Tax
        itemTotalText=element.replace("Item total: $","")
        itemTotal=float(itemTotalText)
        print(itemTotal)

        # Calculate Item Total plus Tax
        ItemTotalPlusTax=itemTotal+(itemTotal*0.08)
        print(ItemTotalPlusTax)


        # Resolve Total
        element2 = wait.until(EC.element_to_be_clickable((By.XPATH, self.label_Total_xpath))).text
        totalText = element2.replace("Total: $", "")
        Total = float(totalText)
        print(Total)

        if ItemTotalPlusTax == Total:
            assert True
        else:
            assert False





