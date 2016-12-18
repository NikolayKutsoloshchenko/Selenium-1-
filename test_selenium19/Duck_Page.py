from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import choice

class duck_page():
    def __init__(self,driver):
        self.driver= driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_to_cart(self):
        Add_to_cart = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="add_cart_product"]')))
        number = int(self.driver.find_element_by_css_selector('span.quantity').get_attribute('textContent'))
        Add_to_cart.click()
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.quantity'), str(number + 1)))

    @property
    def choose_size(self):
        return self.driver.find_elements_by_css_selector('select[name="options[Size]"]')

    def choose(self, select_size):
        select_size[0].click()
        select_size[0].send_keys(Keys.ARROW_DOWN)
        select_size[0].send_keys(Keys.ENTER)