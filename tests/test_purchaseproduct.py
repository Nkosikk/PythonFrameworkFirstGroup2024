import allure
import pytest

from pageObjects.homePage import HomePage
from tests.conftest import setup


class Test_002_HomePageToSauceDemo:
    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.BLOCKER)
    def test_HomeTests(self, setup):
       self.driver = setup
       self.hp = HomePage(self.driver)
       self.hp.button_addtocart_id()
       allure.attach(self.driver.get_screenshot_as_png(), name="Product Page", attachment_type=AttachmentType.PNG)