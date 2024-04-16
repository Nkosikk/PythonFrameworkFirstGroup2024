from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    label_product_xpath = "//span[@class='title'][contains(.,'Products')]"


    def __init__(self, driver):
        self.driver = driver

    # def enterUsername(self, username):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((By.ID, self.textbox_username_id)))
    #     element.send_keys(username)
