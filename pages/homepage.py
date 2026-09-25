from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self,browser):
        self.browser = browser

    def open(self):

        self.browser.get('https://demoblaze.com/index.html')

    def click_galaxy_s6(self):

        samsungname = self.browser.find_element(By.XPATH,"//a[text()='Samsung galaxy s6']")
        
        samsungname.click()
        
    def click_monitor(self):
        monitors_link = self.browser.find_element(By.CSS_SELECTOR,'''[onclick="byCat('monitor')"]''')
        monitors_link.click()
   
         
        
