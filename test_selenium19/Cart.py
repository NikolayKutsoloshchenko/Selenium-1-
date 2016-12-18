from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class cart():
    def __init__(self,driver):
        self.driver= driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        if self.driver.current_url != 'http://localhost/litecart/en/checkout':
          self.driver.find_element_by_css_selector('div#cart a.link').click()
          self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'td.item')))
        return self

    def delete_product(self):
        table = self.driver.find_element_by_css_selector('table [class= "dataTable rounded-corners"]')
        Remove_button = self.driver.find_element_by_css_selector('button[name="remove_cart_item"]')
        Remove_button = self.wait.until(EC.visibility_of(Remove_button))
        Remove_button.click()
        self.wait.until(EC.staleness_of(table))

    @property
    def number_of_ducks(self):
        return len(self.driver.find_elements_by_css_selector('td.item'))