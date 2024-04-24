from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    username_id = "user-name"
    password_id = "password"
    login_id = "login-button"
    loginError_xpath = "//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]"

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.username_id)))
        element.send_keys(username)

    def enterPassword(self, password):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.password_id)))
        element.send_keys(password)

    def clickLoginButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.login_id)))
        element.click()
