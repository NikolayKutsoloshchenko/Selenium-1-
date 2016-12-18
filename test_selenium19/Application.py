from selenium import webdriver
from Cart import cart
from Main_page import main_page
from Duck_Page import duck_page



class application():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.cart = cart(self.driver)
        self.main_page = main_page(self.driver)
        self.duck_page = duck_page(self.driver)

    def quit(self):
        self.driver.quit()

    def add_3_ducks(self):
        for i in range(3):
            self.main_page.open().click_any_duck()
            size = self.duck_page.choose_size
            if size:
                self.duck_page.choose(size)
            self.duck_page.add_to_cart()

    def delete_all_ducks(self):
        self.cart.open()
        number = self.cart.number_of_ducks
        for n in range(number):
            self.cart.delete_product()

    @property
    def items_in_bag(self):
        return self.cart.open().number_of_ducks