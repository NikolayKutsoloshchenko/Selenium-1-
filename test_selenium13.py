#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.get('http://localhost/litecart/')
    request.addfinalizer(driver.quit)
    return driver

def test_adding_to_cart (driver):
    for i in range(1,4):
      add_duck(driver,i)
    Checkout = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div#cart a.link')))
    Checkout.click()
    number_of_items = len(driver.find_elements_by_css_selector('td.item')) # Может быть такое что одна и та же утка выбранна несколько раз
    for i in range(number_of_items):
      delete_duck(driver)

def delete_duck(driver):
    table = driver.find_element_by_css_selector('table [class= "dataTable rounded-corners"]')
    Remove_button = driver.find_element_by_css_selector('button[name="remove_cart_item"]')
    Remove_button = WebDriverWait(driver,15).until(EC.visibility_of(Remove_button))
    Remove_button.click()
    WebDriverWait(driver,10).until(EC.staleness_of(table))



def add_duck(driver, number):
    ducks = driver.find_elements_by_css_selector('div#box-most-popular li')
    ducks[number].click()
    Wait= WebDriverWait(driver,10)
    Add_to_cart = Wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[name="add_cart_product"]')))
    select_size = driver.find_elements_by_css_selector('select[name="options[Size]"]')
    # У некоторых уток есть размер. Если он есть - то выберем первый
    if len(select_size) > 0:
        select_size[0].click()
        select_size[0].send_keys(Keys.ARROW_DOWN)
        select_size[0].send_keys(Keys.ENTER)
    Add_to_cart.click()
    Wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'span.quantity'), str(number)))
    driver.find_element_by_css_selector('div#logotype-wrapper').click()
