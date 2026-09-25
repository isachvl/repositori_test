from selenium.webdriver.common.by import By
from pages.homepage import HomePage

from pages.product import ProductPage
import time



def test_open_s6(open_browser):
    homepage=HomePage(open_browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(open_browser)

    product_page.check_title_is('Samsung galaxy s6')
     

def test_count_monitors(open_browser):

    homepage=HomePage(open_browser)
    homepage.open()

    homepage.click_monitor()
    time.sleep(5)
    product_page = ProductPage(open_browser)

    product_page.chec_product_count(2)
    


