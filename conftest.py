
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def open_browser():
    #browser = webdriver.Firefox()
    #browser.maximize_window()

    options = Options()
    options.add_argument('--headless')#new
    options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"

    browser = webdriver.Firefox(options=options)

    browser.implicitly_wait(3)

    yield browser

    browser.close()