import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
    if browser.lower() or browser.upper() == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')  # Run in headless mode
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        print("Chrome Browser launched successfully")

    elif browser.lower() or browser.upper() == 'firefox':
        driver = webdriver.Firefox()
        print("Firefox Browser launched successfully")

    else:
        driver = webdriver.Edge()
        print("Edge Browser launched successfully")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
