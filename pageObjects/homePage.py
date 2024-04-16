import time
from logging import root
from operator import contains
from telnetlib import EC
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    button_addtocart_id = "add-to-cart-sauce-labs-backpack"
    def __init__(self, driver):
        self.driver = driver
        def clickAddToCartButton(self):
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.ID, self.button_addtocart_id)))
            element.click()