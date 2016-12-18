from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import choice

class main_page():
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get('http://localhost/litecart/en/')
        return  self

    def click_any_duck(self):
        ducks = self.driver.find_elements_by_css_selector('div#box-most-popular li')
        choice(ducks).click()