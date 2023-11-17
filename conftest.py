import webbrowser
import time

import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get('https://www.ukr.net/')
    time.sleep(5)
    yield driver
    time.sleep(5)
    driver.quit()


@pytest.fixture()
def browser_1():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')
    time.sleep(5)
    yield driver
    time.sleep(8)
    driver.quit()
